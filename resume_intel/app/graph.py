from langgraph.graph import END, StateGraph
from pydantic import BaseModel

from app.models import AnalysisResult, ExperienceSummary, Resume, Skill
from app.services.extractors import extract_experience, extract_skills
from app.services.summarizer import summarize_resume


# Use a Pydantic BaseModel as the graph state
class ResumeStateModel(BaseModel):
    resume: Resume
    text: str | None = None
    skills: list[Skill] | None = None
    years: float | None = None
    summary: str | None = None


# Build graph (module-level)
graph = StateGraph(ResumeStateModel)


async def parse_node(state: ResumeStateModel) -> ResumeStateModel:
    state.text = state.resume.text
    return state


async def extract_node(state: ResumeStateModel) -> ResumeStateModel:
    text = state.text or ""
    state.skills = await extract_skills(text)
    state.years = await extract_experience(text)
    return state


async def summarize_node(state: ResumeStateModel) -> ResumeStateModel:
    state.summary = await summarize_resume(state.text or "", state.skills or [])
    return state


async def format_node(state: ResumeStateModel) -> AnalysisResult:
    return AnalysisResult(
        summary=state.summary or "",
        skills=state.skills or [],
        experience=ExperienceSummary(
            years_experience=state.years,
            roles=["ML Engineer", "Backend Developer"],
        ),
    )


graph.add_node("parse", parse_node)
graph.add_node("extract", extract_node)
graph.add_node("summarize", summarize_node)
graph.add_node("format", format_node)
graph.add_edge("parse", "extract")
graph.add_edge("extract", "summarize")
graph.add_edge("summarize", "format")
graph.add_edge("format", END)

compiled_graph = graph.compile()
