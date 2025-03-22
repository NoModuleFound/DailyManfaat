
from typing import Annotated
from datetime import datetime
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy import (
    CheckConstraint, Column, Enum,
    ForeignKey, Index, Integer,
    MetaData, PrimaryKeyConstraint,
    String, Table, text, func
)

from .config import settings



async_engine = create_async_engine(
    url=settings.DATABASE_URL,
    echo=True,
)

async_session_factory = async_sessionmaker(async_engine)

intpk = Annotated[int, mapped_column(primary_key=True)]
str_32 = Annotated[str, 32]
str_64 = Annotated[str, 64]
str_256 = Annotated[str, 256]
str_512 = Annotated[str, 512]

time_now = Annotated[datetime, mapped_column(default=func.now())]
update_time = Annotated[datetime, mapped_column(onupdate=func.now())]


class Base(DeclarativeBase):
    type_annotation_map = {
        str_256: String(256),
        str_512: String(512),
        str_32: String(32),
        str_64: String(64)
    }

    def __repr__(self):

        columns = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return f"<{self.__class__.__name__}({columns})>"

    def __str__(self):
        return self.__repr__()