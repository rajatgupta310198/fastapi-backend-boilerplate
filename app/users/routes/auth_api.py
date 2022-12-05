from fastapi import APIRouter, status
from fastapi.responses import JSONResponse


auth_api = APIRouter(prefix="/auth", tags=["Authentication APIs"])



@auth_api.post('/login')
def login():
    return JSONResponse(content={}, status_code=status.HTTP_200_OK)