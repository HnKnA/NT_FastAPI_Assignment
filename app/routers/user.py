from uuid import UUID
from starlette import status
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_db_context, get_db_context
from models.user import SearchUserModel, UserModel, UserViewModel
from services import user as UserService
from schemas.user import User
from services import auth as AuthService
from services.exception import *

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=list[UserViewModel])
async def get_all_users(
    username: str = Query(default=None),
    company_id: UUID = Query(default=None),
    page: int = Query(ge=1, default=1),
    size: int = Query(ge=1, le=50, default=10),
    async_db: AsyncSession = Depends(get_async_db_context),
    user: User = Depends(AuthService.token_interceptor),
    ):
    
    if not user.is_admin:
        raise AccessDeniedError()
        
    conds = SearchUserModel(username, company_id, page, size)
    return await UserService.get_users(async_db, conds)


@router.get("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserViewModel)
async def get_user_by_id(
    user_id: UUID,
    db: Session = Depends(get_db_context),
    current_user: User = Depends(AuthService.token_interceptor)
    ): 
    
    if not current_user.is_admin and current_user.id != user_id:
        raise AccessDeniedError()
       
    user = UserService.get_user_by_id(db, user_id)
    
    if user is None:
        raise ResourceNotFoundError()

    return user


@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserViewModel)
async def create_user(request: UserModel, db: Session = Depends(get_db_context)):
    return UserService.add_new_user(db, request)


@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserViewModel)
async def update_user(
    user_id: UUID,
    request: UserModel,
    db: Session = Depends(get_db_context),
    current_user: User = Depends(AuthService.token_interceptor)
    ):
    
    if not current_user.is_admin and current_user.id != user_id:
        raise AccessDeniedError()
    
    user = UserService.get_user_by_id(db, user_id)

    if user is None:
        raise ResourceNotFoundError()
        
    return UserService.update_user(db, user_id, request)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: UUID,
    db: Session = Depends(get_db_context),
    current_user: User = Depends(AuthService.token_interceptor)
    ):
    
    if not current_user.is_admin and current_user.id != user_id:
        raise AccessDeniedError()
    
    user = UserService.get_user_by_id(db, user_id)
    
    if user is None:
        raise ResourceNotFoundError()

    UserService.delete_user(db, user_id)
