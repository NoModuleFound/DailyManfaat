from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from src.users.models import UserORM
from src.users.schemas import *

from src.database.manager import async_session_factory

from src.authorization.schemas import BasicLogin
from src.authorization.utils import hash_password, encode_jwt, verify_password

from .exceptions import IncorrectCredentials, UserAlreadyExists

class AuthService:
    @staticmethod
    async def create_user(user_data: BasicLogin):
        async with async_session_factory() as session:
            try:
                new_user = UserORM(
                    first_name=user_data.first_name,
                    last_name=user_data.last_name,
                    email=user_data.email,
                    password_hash=hash_password(user_data.password)
                )
                session.add(new_user)
                await session.commit()
                await session.refresh(new_user)
                orm_data = {k: v for k, v in new_user.__dict__.items() if not k.startswith('_')}
                return UserBase.model_validate(orm_data)
            except IntegrityError:
                raise UserAlreadyExists


    @staticmethod
    async def check_user_creds_bool(user_creds: BasicLogin) -> bool:
        async with async_session_factory() as session:
            try:
                result = await session.execute(
                    select(UserORM).where(UserORM.email == user_creds.email)
                )
                user = result.scalars().first()
                if not user:
                    raise IncorrectCredentials
                
                if not verify_password(password=user_creds.password, hashed_password=user.password_hash):
                    raise IncorrectCredentials
                
                return True

            except IncorrectCredentials:
                raise
            except Exception as e:
                raise RuntimeError(f"Error during user authentication: {str(e)}")


    @staticmethod
    async def check_user_creds(user_creds: BasicLogin):
        async with async_session_factory() as session:
            try:
                result = await session.execute(
                    select(UserORM).where(UserORM.email == user_creds.email)
                )
                user = result.scalars().first()
                if not user:
                    raise IncorrectCredentials
                
                if not verify_password(password=user_creds.password, hashed_password=user.password_hash):
                    raise IncorrectCredentials
                
                try:
                    orm_data = {k: v for k, v in user.__dict__.items() if not k.startswith('_')}
                    user_data = UserDTO.model_validate(orm_data).model_dump()
                    return encode_jwt({"user_data": user_data}, exp_time=3600)
                except Exception as e:
                    raise RuntimeError(f"Failed to generate JWT token: {str(e)}")
                    
            except IncorrectCredentials:
                raise
            except Exception as e:
                raise RuntimeError(f"Error during user authentication: {str(e)}")
