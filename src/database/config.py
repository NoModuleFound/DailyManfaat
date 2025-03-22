from pydantic_settings import BaseSettings



class Settings(BaseSettings):

  @property
  def DATABASE_URL(self) -> str:
    return "sqlite+aiosqlite:///db.sqlite"

settings = Settings()