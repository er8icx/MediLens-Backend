
from .build_graph import build_graph

class GraphRunner:
    def __init__(self):
        self.graph = build_graph()
        
    async def run(self, query: str):
        print(f"Running graph for: {query}")
        return {"result": "Graph execution result"}
