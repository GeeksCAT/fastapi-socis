from sqlalchemy.orm import Session

import bcrypt
from app import models, schemas
from dateutil.relativedelta import relativedelta


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(
        email=user.email,
        # username=user.username,  # to be uncommented
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


#########################

def get_acts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Act).offset(skip).limit(limit).all()

def get_acts_by_user(db: Session, user: schemas.User):
    return db.query(models.Act).filter(models.Act.owner == user).all()

def create_act(db: Session, act: schemas.ActCreate, user: schemas.User):
    db_act = models.Act(
        name=act.name,
        description=act.description,
        link=act.link,
        user_id=user.id
    )
    db.add(db_act)
    db.commit()
    db.refresh(db_act)
    return db_act