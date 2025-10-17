# app.py

from typing import Literal, TypedDict, cast

from langgraph.graph import END, START, StateGraph


class State(TypedDict, total=False):
    input: str
    output: str
    task: Literal["calc", "format"]


def detect_task(state: State) -> State:
    input_text = state["input"]
    task: Literal["calc", "format"] = cast(
        Literal["calc", "format"],
        "calc" if any(ch.isdigit() for ch in input_text) else "format",
    )
    print(f"Detected task: {task}")
    return {**state, "task": task}


def calculator_node(state: State) -> State:
    expr = state["input"]
    try:
        result = eval(expr)
    except Exception as e:
        result = f"Error: {e}"
    print(f"Calculated: {result}")
    return {**state, "output": f"Result: {result}"}


def reformatter_node(state: State) -> State:
    text = state["input"]
    print(f"Reformatted: {text.upper()}")
    return {**state, "output": text.upper()}


def main():
    graph = StateGraph(State)
    graph.add_node("detect_task", detect_task)
    graph.add_node("calc", calculator_node)
    graph.add_node("format", reformatter_node)

    graph.add_edge(START, "detect_task")
    graph.add_conditional_edges(
        "detect_task",
        lambda state: state["task"],
        {"calc": "calc", "format": "format"},
    )
    graph.add_edge("calc", END)
    graph.add_edge("format", END)

    app = graph.compile()

    print("\n--- Run 1 ---")
    result1 = app.invoke({"input": "2 + 2"})
    print("Final result:", result1)

    print("\n--- Run 2 ---")
    result2 = app.invoke({"input": "hello world"})
    print("Final result:", result2)


if __name__ == "__main__":
    main()
