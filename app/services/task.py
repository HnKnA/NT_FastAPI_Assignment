from typing import List
from uuid import UUID
from sqlalchemy import select
from sqlalchemy.orm import Session, joinedload
from schemas.task import Task
from models.task import TaskModel, SearchTaskModel
from services import user as UserService
from services.utils import get_current_utc_time
from services.exception import ResourceNotFoundError, InvalidInputError


def get_tasks(db: Session, conds: SearchTaskModel) -> List[Task]:
    # Default of joinedload is LEFT OUTER JOIN
    query = select(Task).options(
        joinedload(Task.owner, innerjoin=True))
    
    if conds.owner_id is not None:
        query = query.filter(Task.owner_id == conds.owner_id)
    
    query = query.offset((conds.page-1)*conds.size).limit(conds.size)
    
    return db.scalars(query).all()


def get_task_by_id(db: Session, id: UUID, /, joined_load = False) -> Task:
    query = select(Task).filter(Task.id == id)
    
    if joined_load:
        query.options(joinedload(Task.owner, innerjoin=True))
    
    return db.scalars(query).first()
    

def add_new_task(db: Session, data: TaskModel) -> Task:
    user = UserService.get_user_by_id(db, data.owner_id)
        
    if user is None:
        raise InvalidInputError("Invalid user information")

    task = Task(**data.model_dump())
    task.created_at = get_current_utc_time()
    task.updated_at = get_current_utc_time()

    db.add(task)
    db.commit()
    db.refresh(task)
    
    return task

def update_task(db: Session, id: UUID, data: TaskModel) -> Task:
    task = get_task_by_id(db, id)

    if task is None:
        raise ResourceNotFoundError()

    if data.owner_id != task.owner_id:
        user = UserService.get_user_by_id(db, data.owner_id)
        if user is None:
            raise InvalidInputError("Invalid user information")
        
        task.owner = user
        task.owner_id = data.owner_id
    
    task.summary = data.summary
    task.description = data.description
    task.status = data.status
    task.priority = data.priority
    task.updated_at = get_current_utc_time()
    
    db.commit()
    db.refresh(task)
    
    return task

def delete_task(db: Session, id: UUID) -> None:
    task = get_task_by_id(db, id)

    if task is None:
        raise ResourceNotFoundError()
    
    db.delete(task)
    db.commit()
