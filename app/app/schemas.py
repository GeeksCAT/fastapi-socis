from typing import List, Optional, Union
from pydantic import BaseModel, EmailStr
from datetime import datetime, date


class UserBase(BaseModel):
    email: EmailStr
    username: Optional[str]  # to be commented


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


class ActBase(BaseModel):
    name: str


class ActCreate(ActBase):
    name: str
    description: str
    link: str
    user_email: EmailStr


class ActQuery(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]


class Act(ActBase):
    id: int
    description: str
    link: str
    owner: User
    created_at: datetime

    class Config:
        orm_mode = True
