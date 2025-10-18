from typing import Annotated, TypedDict

from langchain.schema import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages


# Annotated allows us to attach extra metadata
# (like how to merge or validate a field) to a type without changing its core type definition.
class MemoryState(TypedDict):  # MemoryState inherits from TypedDict
    messages: Annotated[list[HumanMessage], add_messages]
    response: str


# reply_node – generates a new message
def reply_node(state: MemoryState) -> MemoryState:
    # Access the last user message
    user_msg = state["messages"][-1].content
    # Generate a response
    response = f"Got it! You said: '{user_msg}'."
    return {**state, "response": response}  # Old state is kept, response is reassigned


# reflect_node – reflects on the conversation so far
def reflect_node(state: MemoryState) -> MemoryState:
    # Count number of messages so far
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
    app.checkpointer = InMemorySaver()  # <- attach a checkpointer

    # Define a thread_id for the conversation
    thread_id = "conversation_1"

    # Config required for checkpointer
    config = {
        "thread_id": thread_id,
        "checkpoint_ns": "default",
        "checkpoint_id": thread_id,
    }

    # First input
    state = {"messages": [HumanMessage(content="Hello!")], "response": ""}
    print(f"User: {state['messages'][-1].content}")  # print the current message
    result = app.invoke(state, config=config)
    print(f"Bot: {result['response']}")

    # Add another message — memory persists
    state["messages"].append(HumanMessage(content="How are you?"))
    print(f"User: {state['messages'][-1].content}")  # print the current message
    result2 = app.invoke(state, config=config)
    print(f"Bot: {result2['response']}")

    # Third message
    state["messages"].append(HumanMessage(content="What’s up?"))
    print(f"User: {state['messages'][-1].content}")  # print the current message
    result3 = app.invoke(state, config=config)
    print(f"Bot: {result3['response']}")


if __name__ == "__main__":
    main()
