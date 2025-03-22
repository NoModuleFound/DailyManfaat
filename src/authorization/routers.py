from typing import Annotated
from fastapi import APIRouter, Body


from .services import AuthService
from .schemas import BasicLogin
from .exceptions import IncorrectCredentials, UserAlreadyExists

from src.system.schemas import ApiResponse
from src.users.schemas import *

router = APIRouter(
    prefix="/auth",
    tags=["Authorization Management"]
)


@router.post("/sign-in", response_model=ApiResponse, summary="Login")
async def user_login(user_creds: Annotated[BasicLogin, Body()]):
    try:
        jwt_token = await AuthService.check_user_creds(user_creds)
        return ApiResponse(status=200, msg="Login successful", details={"token": jwt_token})
    except IncorrectCredentials:
        return ApiResponse(status=401, msg="Incorrect Credentials")


@router.post("/sign-up", response_model=ApiResponse, summary="Register")
async def user_sign_up(user_data: Annotated[UserAddDTO, Body()]):
    """Register a new user and return their details."""
    try:
        new_user = await AuthService.create_user(user_data)
        return ApiResponse(status=201, msg="User created successfully", details={"user_data": new_user})
    except UserAlreadyExists:
        return ApiResponse(status=409, msg="User already exists")