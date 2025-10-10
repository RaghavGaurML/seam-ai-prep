from pydantic import BaseModel, EmailStr, Field, field_validator


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    email: EmailStr


class Job(BaseModel):
    id: int
    title: str
    description: str | None
    skills: list[str] = []


class Resume(BaseModel):
    user_id: int
    summary: str | None
    experience_years: int = Field(..., ge=0)
    skills: list[str]

    @field_validator("skills")
    def must_have_skills(cls, v):
        if not v:
            raise ValueError("At least one skill required.")
        return v
