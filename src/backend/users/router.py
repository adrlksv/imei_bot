from fastapi import APIRouter, Response, Depends

from src.backend.users.auth import authenticate_user, create_access_token, get_password_hash
from src.backend.users.dependencies import get_current_user
from src.backend.users.schemas import SUserRegister, SUserLogin
from src.backend.users.dao import UserDAO
from src.backend.users.models import User

from src.backend.exceptions import UserAlreadyExistsException, IncorrectEmailOrPasswordException


router = APIRouter(
    prefix="/auth",
    tags=["Auth"],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserDAO.find_one_or_none(email=user_data.email)

    if existing_user:
        raise UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UserDAO.add(
        email=user_data.email,
        login=user_data.login,
        hashed_password=hashed_password
    )


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise IncorrectEmailOrPasswordException
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("imei_access_token", access_token, httponly=True)
    return access_token


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie("imei_access_token")


@router.get("/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user
