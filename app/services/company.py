from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session
from schemas.company import Company

def get_companies(db: Session) -> list[Company]:
    return db.scalars(select(Company).order_by(Company.created_at)).all()

def get_company_by_id(db: Session, company_id: UUID) -> Company:
    return db.scalars(select(Company).filter(Company.id == company_id)).first()
    