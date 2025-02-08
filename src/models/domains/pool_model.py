from pydantic import BaseModel
from typing import List
from enum import Enum

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
    volume: float
    material: MaterialEnum
    heating_type: HeatingTypeEnum
    maintenance_frequency: MaintenanceFrequencyEnum
    notes: List[str]