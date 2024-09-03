from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field

from schemas.company import Mode


class CompanyModel(BaseModel):
    name: str
    description: Optional[str]
    rating: int = Field(ge=0, le=5, default=0)
    mode: Mode = Field(default=Mode.ACTIVE)
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Cong ty TNHH ABC",
                "description": "Description for ABC company",
                "rating": 2,
                "mode": "Active"
            }
        }

class CompanyViewModel(BaseModel):
    id: UUID
    name: str
    description: str | None = None
    mode: Mode
    rating: int
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True