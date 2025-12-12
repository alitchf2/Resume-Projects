from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from ..controllers import system as controller
from ..dependencies.database import get_db

router = APIRouter(
    tags=['System'],
    prefix="/system"
)


@router.post("/setup", status_code=status.HTTP_201_CREATED)
def setup_database(db: Session = Depends(get_db)):
    return controller.setup_database(db=db)