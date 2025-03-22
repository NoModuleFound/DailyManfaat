from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, Field


class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file="src/email/.env",
    env_file_encoding="utf-8"
  )

  EMAIL: EmailStr = Field(min_length=8)
  PASSWORD: str

settings = Settings()