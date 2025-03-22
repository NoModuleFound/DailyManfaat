from pydantic import EmailStr, Field
from typing import Optional, List

from src.PyModel import BaseModel


# === Базовая схема пользователя ===
class UserBase(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None


# === DTO для передачи данных (ответ API) ===
class UserDTO(UserBase):
    """DTO для передачи данных о пользователе"""
    id: int
    email: EmailStr = Field(min_length=8)


# === DTO для создания пользователя (запрос API) ===
class UserAddDTO(UserBase):
    """DTO для создания нового пользователя"""
    email: EmailStr
    password: str = Field(min_length=8)


# === DTO для обновления пользователя (запрос API) ===
class UserUpdateDTO(UserBase):
    """DTO для обновления данных пользователя"""
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
