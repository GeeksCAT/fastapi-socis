from app import crud, schemas
from app.api import deps
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/", response_model=list[schemas.Act])
def read_acts(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    acts = crud.get_acts(db, skip=skip, limit=limit)
    return acts


@router.post("/create", response_model=schemas.Act)
def create_act(act: schemas.ActCreate, db: Session = Depends(deps.get_db)):
    db_user = crud.get_user_by_email(db, act.user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    act = crud.create_act(db, act, db_user)
    return act


@router.post("/", response_model=list[schemas.Act])
def read_acts_by_user(act_query: schemas.ActQuery, db: Session = Depends(deps.get_db)):
    db_user =  crud.get_user_by_email(db, act_query.email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.get_acts_by_user(db, db_user)
