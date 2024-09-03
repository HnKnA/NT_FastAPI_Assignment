from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel
from models.company import CompanyViewModel

class SearchUserModel():
    def __init__(self, username, company_id, page, size) -> None:
        self.username = username
        self.company_id = company_id
        self.page = page
        self.size = size
        
        
class UserModel(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str
    hashed_password: str
    company_id: Optional[UUID] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "Tuan Hai",
                "email": "ninjago@gmail.com",
                "first_name": "Hau",
                "last_name": "Hoang",
                "company_id": "313e4567-e89b-12d3-a456-426614174000",
                "hashed_password": "Your hashed password here",
            }
        }

class UserBaseModel(BaseModel):
    id: UUID
    username: str
    email: str | None = None
    first_name: str
    last_name: str
    
    class Config:
        from_attributes = True
        arbitrary_types_allowed = True

class UserViewModel(UserBaseModel):
    is_admin: bool
    company_id: UUID | None = None
    company: CompanyViewModel | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None