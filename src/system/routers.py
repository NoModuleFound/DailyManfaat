from fastapi import APIRouter, Body
from .schemas import SecretKey
from typing import Annotated
from .config import settings
from src.database.orm import AsyncORM
from .schemas import ApiResponse

router = APIRouter(prefix='/system',
                  tags=['System Management'])


@router.post('/setup-db')
async def drop_database(secret_key: Annotated[SecretKey, Body()] ):
  if secret_key.password == settings.SECRET_KEY:
    await AsyncORM.drop_db()
    await AsyncORM.create_db()
    return ApiResponse(msg='Successfully dropped and created DB')
  return ApiResponse(status=406, msg='Incorrect Secret Key')
