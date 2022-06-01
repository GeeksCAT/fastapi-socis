from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps


router = APIRouter()


@router.get("/", response_model=list[schemas.Enrolment])
def read_enrolments(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    enrolments = crud.get_enrolments(db, skip=skip, limit=limit)
    return enrolments


@router.post("/", response_model=schemas.Enrolment)
def create_enrolment(enrolment: schemas.EnrolmentCreate, db: Session = Depends(deps.get_db)):
    db_user = crud.get_user_by_email(db, enrolment.user_email) or crud.get_user_by_username(db, enrolment.username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    enrolment = crud.create_enrolment(db, enrolment, db_user)
    return enrolment


@router.post("/", response_model=list[schemas.Enrolment])
def read_enrolments_by_user(enrolquery: schemas.EnrolmentQuery, db: Session = Depends(deps.get_db)):
    if enrolquery.start_date:
        return crud.filter_by_date(db, enrolquery.start_date)
    db_user = crud.get_user_by_username(db, enrolquery.username) or crud.get_user_by_email(db, enrolquery.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_enrolments_by_user(db, db_user)