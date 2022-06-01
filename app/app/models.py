from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base_class import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    username = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())

    # User may have many Enrolments
    acts = relationship("Act", back_populates="owner")


class Act(Base):
    __tablename__ = "act"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    link = Column(String)
    created_at = Column(DateTime, default=func.now())

    user_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="acts")
