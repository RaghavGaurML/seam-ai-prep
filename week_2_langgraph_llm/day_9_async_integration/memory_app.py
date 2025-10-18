from typing import Annotated, TypedDict

from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages


# Annotated allows us to attach extra metadata
# (like how to merge or validate a field) to a type without changing its core type definition.
class MemoryState(TypedDict):  # MemoryState inherits from TypedDict
    messages: Annotated[list, add_messages]
    response: str


# reply_node – generates a new message
def reply_node(state: MemoryState) -> MemoryState:
    user_msg = state["messages"][-1]["content"]
    response = f"Got it! You said: '{user_msg}'."
    return {**state, "response": response}  # Old state is kept, response is reassigned


# reflect_node – reflects on the conversation so far
def reflect_node(state: MemoryState) -> MemoryState:
    count = len(state["messages"])
    reflection = f"So far, we’ve exchanged {count} messages."
    return {**state, "response": reflection}


# We’ll use a simple flow: start → reply → reflect → END
def build_graph():
    # StateGraph expects a type (like a TypedDict) that defines the shape of the state,
    # so it knows which keys exist, their types, and how to merge updates between nodes.
    graph = StateGraph(MemoryState)

    graph.add_node("reply", reply_node)
    graph.add_node("reflect", reflect_node)

    # Setting an entrypoint like "reply" lets the graph start execution there,
    # so we don’t need to use the special START node when there’s only one starting node.
    graph.set_entry_point("reply")
    graph.add_edge("reply", "reflect")
    graph.add_edge("reflect", END)

    return graph.compile()


def main():
    # Day 9 adds memory to accumulate state over time (e.g., messages),
    # while Day 8 only handles branching without persistent state.
    app = build_graph()

    # First input
    state = {"messages": [{"role": "user", "content": "Hello!"}]}
    result = app.invoke(state)
    print(result["response"])

    # Add another message — memory persists
    new_state = app.update_state(
        state, {"messages": [{"role": "user", "content": "How are you?"}]}
    )
    result2 = app.invoke(new_state)
    print(result2["response"])


if __name__ == "__main__":
    main()
