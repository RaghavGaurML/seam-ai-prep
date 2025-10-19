from pydantic import BaseModel, Field


class Skill(BaseModel):
    name: str
    confidence: float = Field(ge=0, le=1)  # greater than 0, less than 1


class ExperienceSummary(BaseModel):
    years_experience: float | None
    roles: list[str]


class Resume(BaseModel):
    text: str
    candidate_name: str | None = None  # <- Examine later


class AnalysisResult(BaseModel):
    summary: str
    skills: list[Skill]
    experience: ExperienceSummary
