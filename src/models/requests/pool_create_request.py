from pydantic import BaseModel

class PoolCreateRequest(BaseModel):
    name: str
    location: str
    volume: float
    material: str
    heating_type: str
    maintenance_frequency: str