
from typing import TypedDict, Annotated, List, Union

class AgentState(TypedDict):
    query: str
    documents: List[str]
    answer: str
