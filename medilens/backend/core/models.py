
from pydantic import BaseModel
from typing import List, Optional

class SearchQuery(BaseModel):
    query: str
    max_results: int = 5

class AgentResponse(BaseModel):
    answer: str
    sources: List[str] = []
    
class DrugInfo(BaseModel):
    name: str
    description: Optional[str] = None
