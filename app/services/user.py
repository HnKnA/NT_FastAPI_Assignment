from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from services.company import get_company_by_id
from services import utils
from models.user import SearchUserModel, UserModel
from schemas.user import User
from services.exception import ResourceNotFoundError
from schemas.user import get_password_hash

async def get_users(async_db: AsyncSession, conds: SearchUserModel) -> list[User]:
    # Default of joinedload is LEFT OUTER JOIN
    query = select(User).order_by(User.created_at).options(
        joinedload(User.company))
    
    if conds.username is not None:
        query = query.filter(User.username.like(f"{conds.username}%"))
    if conds.company_id is not None:
        query = query.filter(User.company_id == conds.company_id)
    
    query = query.offset((conds.page - 1) * conds.size).limit(conds.size)
    
    result = await async_db.scalars(query)
    
    return result.all()

def get_user_by_id(db: Session, user_id: UUID) -> User:
    return db.scalars(select(User).filter(User.id == user_id)).first()

def add_new_user(db: Session, data: UserModel) -> User:
    user = User(**data.model_dump())

    user.hashed_password = get_password_hash(data.hashed_password)
    user.created_at = utils.get_current_utc_time()
    user.updated_at = utils.get_current_utc_time()
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    return user

def update_user(db: Session, id: UUID, data: UserModel) -> User:
    user = get_user_by_id(db, id)

    if user is None:
        raise ResourceNotFoundError()
    
    if data.company_id is not None:
        company = get_company_by_id(db, data.company_id)
        
        if company is None:
            raise ResourceNotFoundError("Company not found")
        
        user.company = company
        user.company_id = data.company_id
    
    user.username = data.username
    user.email = data.email
    user.first_name = data.first_name
    user.last_name = data.last_name
    user.updated_at = utils.get_current_utc_time()
    
    db.commit()
    db.refresh(user)

    return user

def delete_user(db: Session, id: UUID) -> None:
    user = get_user_by_id(db, id)

    if user is None:
        raise ResourceNotFoundError()
    
    db.delete(user)
    db.commit()
