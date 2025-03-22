from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file="src/authorization/.env",
    env_file_encoding="utf-8"
  )

  PRIVATE_KEY: str
  PUBLIC_KEY: str
  ALGORITHM: str

settings = Settings()