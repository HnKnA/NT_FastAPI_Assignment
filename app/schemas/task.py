import enum
from sqlalchemy import Column, ForeignKey, SmallInteger, String, Uuid, Enum
from sqlalchemy.orm import relationship
from database import Base
from .base_entity import BaseEntity


class Status(str, enum.Enum):
    DONE = 'D'
    PROGRESSED = 'P'


class Task(BaseEntity, Base):
    __tablename__ = "tasks"

    summary = Column(String)
    description = Column(String)
    status = Column(Enum(Status), nullable=False, default=Status.PROGRESSED)
    priority = Column(SmallInteger, nullable=False, default=0)
    owner_id = Column(Uuid, ForeignKey("users.id"), nullable=True)

    owner = relationship("User", back_populates="tasks")