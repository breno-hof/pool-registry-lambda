from pydantic import BaseModel, field_validator
from typing import List, Optional
from enum import Enum
from decimal import Decimal

class MaterialEnum(str, Enum):
    TILE = "tile"
    FIBERGLASS = "fiberglass"
    VINYL = "vinyl"

class HeatingTypeEnum(str, Enum):
    ELETRIC = "eletric"
    GAS = "gas"
    SOLAR = "solar"

class MaintenanceFrequencyEnum(str, Enum):
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    MONTHLY = "monthly"

class PoolModel(BaseModel):
    pool_id: str
    name: str
    location: str
    volume: Decimal
    material: MaterialEnum
    heating_type: HeatingTypeEnum
    maintenance_frequency: MaintenanceFrequencyEnum
    notes: List[str]

    @field_validator("pool_id", "location", "material", "heating_type", "maintenance_frequency", "name")
    def not_empty(cls, value: Optional[str]) -> Optional[str]:
        if value is None or value.strip() == "":
            raise ValueError("Field shouldn't be empty or blank")
        return value
    
    @field_validator("volume")
    def less_than_zero(cls, value: Optional[float]) -> Optional[float]:
        if value is not None and value <= 0:
            raise ValueError("Field should be equal or greater than zero")
        return value
    
    @field_validator("notes")
    def max_size_list(cls, value: Optional[List[str]]) -> Optional[List[str]]:
        if value is None or len(value) > 10:
            raise ValueError("Notes shouldn't overflows ten items")
        return value
    