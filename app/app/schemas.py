from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr
from datetime import datetime, date


class UserBase(BaseModel):
    email: EmailStr
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


####################


class EnrolmentBase(BaseModel):
    start_date: date


class EnrolmentCreate(EnrolmentBase):
    start_date: date
    username: Optional[str]
    email: Optional[EmailStr]


class EnrolmentQuery(BaseModel):
    start_date: Optional[date]
    username: Optional[str]
    email: Optional[EmailStr]


class Enrolment(EnrolmentBase):
    auto_renew: bool
    end_date: date
    owner: User
    created_at: datetime

    class Config:
        orm_mode = True
