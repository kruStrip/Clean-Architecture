from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_current_admin, get_db
from app.models import User
from app.repositories.user_repo import UserRepository
from app.schemas import UserOut

router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/users", response_model=List[UserOut])
def list_users(db: Session = Depends(get_db), _: User = Depends(get_current_admin)):
    return UserRepository(db).list_all()
