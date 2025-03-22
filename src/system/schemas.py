from pydantic import field_validator, Field
from src.PyModel import BaseModel
from .status_data import status_dict
from typing import Optional, Any


class ApiResponse(BaseModel):
  status: dict[int, str] = {200: "Success"}
  msg: Optional[Any] = None
  details: Optional[Any] = None

  @field_validator("status", mode="before")
  @classmethod
  def set_status(cls, v: int) -> dict[int, str]:
      """Convert status_code to {status_code: status_name}"""
      status_name = status_dict.get(v, "UNKNOWN")
      return {v: status_name}


class SecretKey(BaseModel):
  password: str = Field(min_length=8)

class SystemLogging(BaseModel):
  ...