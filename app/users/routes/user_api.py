from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.deps import get_db

user_api = APIRouter(tags=["User"], prefix="/user")




@user_api.get("/")
def user_list(page: int, page_size: int, db: Session = Depends(get_db)):
    return JSONResponse(content=[], status_code=status.HTTP_200_OK)