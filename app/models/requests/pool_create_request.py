from typing import Optional
from pydantic import BaseModel, field_validator

class PoolCreateRequest(BaseModel):
    name: str
    location: str
    volume: float
    material: str
    heating_type: str
    maintenance_frequency: str

    @field_validator("material", "location", "heating_type", "maintenance_frequency", "name")
    def not_empty(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and value.strip() == "":
            raise ValueError("Field shouldn't be empty or blank")
        return value

    @field_validator("volume")
    def less_than_zero(cls, value: Optional[float]) -> Optional[float]:
        if value is not None and value <= 0:
            raise ValueError("Field should be equal or greater than zero")
        return value
    