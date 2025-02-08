from pydantic import BaseModel
from typing import List

class PoolResponse(BaseModel):
    pool_id: str
    name: str
    location: str
    volume: float
    material: str
    heating_type: str
    maintenance_frequency: str
    notes: List[str]