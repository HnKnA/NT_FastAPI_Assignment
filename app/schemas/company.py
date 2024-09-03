import enum
from sqlalchemy import Column, SmallInteger, String, Enum
from sqlalchemy.orm import relationship
from database import Base
from .base_entity import BaseEntity


class Mode(str, enum.Enum):
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'


class Company(BaseEntity, Base):
    __tablename__ = "companies"

    name = Column(String)
    description = Column(String)
    mode = Column(Enum(Mode), nullable=False, default=Mode.ACTIVE)
    rating = Column(SmallInteger, nullable=False, default=0)

    users = relationship("User", back_populates="company")