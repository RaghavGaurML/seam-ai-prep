import asyncio

from app.models import Skill


async def summarize_resume(resume_text: str, skills: list[Skill]) -> str:
    await asyncio.sleep(0.2)
    skill_list = ", ".join([s.name for s in skills])
    return f"Candidate experienced in {skill_list}. Approx. 3 years in ML development."
