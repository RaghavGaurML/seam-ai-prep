import asyncio

from app.graph import ResumeStateModel, compiled_graph
from app.models import Resume


async def main():
    resume = Resume(
        text="I have 3 years of experience building FastAPI and LangGraph pipelines."
    )
    init_state = ResumeStateModel(resume=resume)
    result = await compiled_graph.ainvoke(init_state)
    # result may already be an AnalysisResult; if graph returns a BaseModel, print `.json()`
    try:
        print(result.json(indent=2))
    except AttributeError:
        # if result is a plain dict
        import json

        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    asyncio.run(main())
