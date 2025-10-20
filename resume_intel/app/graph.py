from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel

from app.models import AnalysisResult, ExperienceSummary, Resume, Skill
from app.services.extractors import extract_experience, extract_skills
from app.services.summarizer import summarize_resume


# --- Input type for entry node ---
class ResumeInput(BaseModel):
    resume: Resume


# --- Full graph state ---
class ResumeStateModel(ResumeInput):
    text: str | None = None
    skills: list[Skill] | None = None
    years: float | None = None
    summary: str | None = None


# Create the StateGraph with the specified schemas
graph: StateGraph[ResumeStateModel, ResumeInput] = StateGraph(
    state_schema=ResumeStateModel
)


# --- Graph nodes ---
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


# --- Add nodes and edges ---
graph.add_node("parse", parse_node)
graph.add_node("extract", extract_node)
graph.add_node("summarize", summarize_node)
graph.add_node("format", format_node)

graph.add_edge(START, "parse")
graph.add_edge("parse", "extract")
graph.add_edge("extract", "summarize")
graph.add_edge("summarize", "format")
graph.add_edge("format", END)

# --- Compile once for reuse ---
compiled_graph = graph.compile()
