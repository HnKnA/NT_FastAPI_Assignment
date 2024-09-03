from uuid import UUID
from starlette import status
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_db_context, get_db_context
from models.company import CompanyModel, CompanyViewModel
from services.exception import ResourceNotFoundError
from services import company as CompanyService

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.get("", response_model=list[CompanyViewModel])
async def get_all_companies(db: Session = Depends(get_db_context)):
    return CompanyService.get_companies(db)


@router.get("/{company_id}", status_code=status.HTTP_200_OK, response_model=CompanyViewModel)
async def get_company_by_id(company_id: UUID, db: Session = Depends(get_db_context)):    
    company = CompanyService.get_company_by_id(db, company_id)

    if company is None:
        raise ResourceNotFoundError()

    return company
