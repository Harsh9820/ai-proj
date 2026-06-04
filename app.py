from langgraph.graph import StateGraph
from state import GraphState
from agent import chatbot_node, researcher_node, writer_node

builder = StateGraph(GraphState)

builder.add_node(
    "researcher",
    researcher_node
)
builder.add_node(
    "writer",
    writer_node
)

builder.set_entry_point("researcher")
builder.add_edge("researcher", "writer")
builder.set_finish_point("writer")

graph = builder.compile()

result = graph.invoke(
    {
        "question": "How does kafka work?"
    }
)

print(result)