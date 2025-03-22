from pydantic import EmailStr, Field
from typing import Any

from src.PyModel import BaseModel


class BasicLogin(BaseModel):
  email: EmailStr
  password: str = Field(min_length=8)

class AdvancedLogin(BaseModel):
  ...

class UserPost(BaseModel):
  token: Any