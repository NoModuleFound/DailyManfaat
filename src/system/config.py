from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
  model_config = SettingsConfigDict(
    env_file="src/system/.env",
    env_file_encoding="utf-8"
  )
  SECRET_KEY: str

settings = Settings()