from typing import List
from pydantic import BaseModel

class PoolUpdateRequest(BaseModel):
    name: str
    heating_type: str
    maintenance_frequency: str
    notes: List[str]