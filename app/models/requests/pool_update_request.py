from typing import List, Optional
from pydantic import BaseModel, field_validator

class PoolUpdateRequest(BaseModel):
    name: Optional[str] = Nul
    heating_type: Optional[str] = None
    maintenance_frequency: Optional[str] = None
    notes: List[str] = []

    @field_validator("heating_type", "maintenance_frequency", "name")
    def not_empty(cls, value: Optional[str]) -> Optional[str]:
        if value is not None and value.strip() == "":
            raise ValueError("Field shouldn't be empty or blank")
        return value
    
    @field_validator("notes")
    def max_size_list(cls, value: Optional[List[str]]) -> Optional[List[str]]:
        if value is not None and len(value) > 10:
            raise ValueError("Notes shouldn't overflows ten items")
        return value