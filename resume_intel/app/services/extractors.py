import asyncio

from app.models import Skill


async def extract_skills(resume_text: str) -> list[Skill]:
    # mock async behavior (replace w/LLM call later)
    await asyncio.sleep(0.2)
    skills = ["Python", "FastAPI", "Pydantic", "LangGraph"]
    return [
        Skill(name=s, confidence=0.9)
        for s in skills
        if s.lower() in resume_text.lower()
    ]


async def extract_experience(resume_text: str) -> float:
    # very niave heuristic example
    await asyncio.sleep(0.2)
    return 3.0 if "experience" in resume_text.lower() else 1.0
