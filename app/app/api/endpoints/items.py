from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import schemas, crud
from api import deps


router = APIRouter()

@router.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(deps.get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

