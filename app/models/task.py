from typing import Optional
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel, Field
from models.user import UserBaseModel
from schemas.task import Status


class SearchTaskModel():
    def __init__(self, owner_id, page, size) -> None:
        self.owner_id = owner_id
        self.page = page
        self.size = size

class TaskModel(BaseModel):
    summary: str
    description: Optional[str]
    priority: int = Field(ge=0, le=5, default=0)
    status: Status = Field(default=Status.PROGRESSED)
    owner_id: Optional[UUID] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "summary": "Task 1",
                "description": "Description for Task 1",
                "priority": 4,
                "owner_id": "123e4567-e89b-12d3-a456-426614174000",
                "status": "P"
            }
        }

class TaskViewModel(BaseModel):
    id: UUID
    summary: str
    description: str | None = None
    status: Status
    priority: int
    owner_id: UUID | None = None
    owner: UserBaseModel | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True