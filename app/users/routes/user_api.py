from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.deps import get_db
from app.users.dto.requests.user_dto import UserSignUpDto

# from app.auth.password_service import PasswordService

user_api = APIRouter(tags=["User"], prefix="/user")


@user_api.post(
    "/signup",
    # response_model=UserResponseDto,
    status_code=status.HTTP_201_CREATED,
)
def sign_up(body: UserSignUpDto, db: Session = Depends(get_db)):
    # user = db.query(User).filter_by(email=body.email).first()
    # if user:
    #     raise AlreadyExistsException(detail="User already exists")
    # password_service = PasswordService()
    # hashed_password: bytes = password_service.encrypt_password(password=body.password)
    # user_db = User(email=body.email, name=body.name, password=hashed_password.decode())
    # db.add(user_db)
    # db.commit()
    # db.refresh(user_db)

    # return user_db
    return {}


@user_api.get("/")
def user_list(page: int, page_size: int, db: Session = Depends(get_db)):
    return JSONResponse(content=[], status_code=status.HTTP_200_OK)
