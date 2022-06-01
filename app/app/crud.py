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
        username=user.username,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_enrolments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Enrolment).offset(skip).limit(limit).all()


def get_enrolments_by_user(db: Session, user:schemas.User):
    return db.query(models.Enrolment).filter(models.Enrolment.owner == user)

def create_enrolment(db: Session, enrolment: schemas.Enrolment, user: schemas.User):
    db_enrolment = models.Enrolment(
        start_date=enrolment.start_date,
        end_date=(enrolment.start_date + relativedelta(years=1)),
        owner_id=user.id
    )
    db.add(db_enrolment)
    db.commit()
    db.refresh(db_enrolment)
    return db_enrolment
