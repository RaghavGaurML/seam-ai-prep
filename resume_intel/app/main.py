# Project Concept: “Resume Intelligence API”
# A small but real AI microservice that:
# -> Takes a resume (text or JSON) and returns structured insights (skills, roles, experience years).
# -> Supports FastAPI endpoints for parsing and matching.
# -> Uses LangGraph for reasoning + extraction flow control.
# -> Employs Pydantic models + typing for data contracts.
# -> Is ready for extension into later “Job Matching” work (Day 13).
from typing import cast

from fastapi import FastAPI

from app.graph import ResumeStateModel, compiled_graph
from app.models import AnalysisResult, Resume

app = FastAPI(title="Resume Intelligence API")


@app.post("/analyze_resume", response_model=AnalysisResult)
async def analyze_resume(resume: Resume):
    state = cast(ResumeStateModel, {"resume": resume})
    result = await compiled_graph.ainvoke(state)
    return result
