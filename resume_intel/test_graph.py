import asyncio
import json

from app.graph import ResumeStateModel, compiled_graph
from app.models import Resume
from pydantic.json import pydantic_encoder


async def main():
    resume = Resume(
        text="I have 3 years of experience building FastAPI and LangGraph pipelines."
    )
    init_state = ResumeStateModel(resume=resume)

    # Run graph
    result = await compiled_graph.ainvoke(init_state)

    # --- Handle output safely ---
    # If it's a Pydantic model, print its .json()
    if hasattr(result, "json"):
        print(result.json(indent=2))
    else:
        # Otherwise, handle dicts containing Pydantic models
        print(json.dumps(result, indent=2, default=pydantic_encoder))


if __name__ == "__main__":
    asyncio.run(main())
