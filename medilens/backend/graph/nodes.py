
from .state import AgentState

def retriever_node(state: AgentState):
    print("Executing retriever node")
    return {"documents": ["doc1", "doc2"]}

def generator_node(state: AgentState):
    print("Executing generator node")
    return {"answer": "Generated answer from graph"}
