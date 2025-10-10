# test_models.py
import pytest
from models import Resume, User
from pydantic import ValidationError


def test_valid_user():
    u = User(id=1, name="Raghav", email="raghav@example.com")
    assert u.email == "raghav@example.com"


def test_invalid_email():
    with pytest.raises(ValidationError):
        User(id=2, name="Fake", email="not-an-email")


def test_resume_requires_skill():
    with pytest.raises(ValidationError):
        Resume(user_id=1, summary="Engineer", experience_years=2, skills=[])
        Resume(user_id=1, summary="Engineer", experience_years=2, skills=[])
