from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.db.base_class import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email) or crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username or Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

##########################


@app.get("/enrolments/", response_model=List[schemas.Enrolment])
def read_enrolments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    enrolments = crud.get_enrolments(db, skip=skip, limit=limit)
    return enrolments

@app.post("/enrolments", response_model=schemas.Enrolment)
def create_enrolment(enrolment: schemas.EnrolmentCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, enrolment.user_email) or crud.get_user_by_username(db, enrolment.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    enrolment = crud.create_enrolment(db, enrolment, db_user)
    return enrolment


@app.post("/enrolments/", response_model=List[schemas.Enrolment])

def read_enrolments_by_user(enrolquery: schemas.EnrolmentQuery, db: Session = Depends(get_db)):
    if enrolquery.start_date:
        return crud.filter_by_date(db, enrolquery.start_date)
    db_user = crud.get_user_by_username(db, enrolquery.username) or crud.get_user_by_email(db, enrolquery.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_enrolments_by_user(db, db_user)