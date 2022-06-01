from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base_class import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now())

    # User may have many Enrolments
    enrolments = relationship("Enrolment", back_populates="owner")


class Enrolment(Base):
    __tablename__ = "enrolment"

    id = Column(Integer, primary_key=True, index=True)
    start_date = Column(Date)
    end_date = Column(Date)
    auto_renew = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())

    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="enrolments")


# class PaymentLog(Base):
#     id
#     amount
#     is_paid
#     requested_at
#     paid_at


# class Event(Base):
#     name
#     description
#     date


# class Act(Base):
#     ___tablename__ = "acts"

#     name
#     description
#     link
#     created_at