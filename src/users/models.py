from sqlalchemy import (Table, Column, Integer, 
                        String, ForeignKey, MetaData,
                        Float, DateTime, Boolean)
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import Annotated
import enum
from datetime import datetime

from src.database.manager import (
    Base, str_32,str_64, str_256, intpk,
    str_512, intpk, update_time, time_now)


# class UserOrm(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     phone = Column(String, unique=False)
#     username = Column(String, unique=True)
#     first_name = Column(String)
#     last_name = Column(String)
#     password_hash = Column(String)
#     public_key = Column(String)
#     last_seen = Column(DateTime)
#     is_online = Column(Boolean)
#     sessions = relationship("Session", back_populates="user")

class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[intpk]
    first_name: Mapped[str_32]
    last_name: Mapped[str_32]
    email: Mapped[str_32] = mapped_column(unique=True)
    phone_number: Mapped[int] = mapped_column(nullable=True, default=None, unique=True)
    password_hash: Mapped[bytes]
    is_active: Mapped[bool] = mapped_column(default=True)
    is_verified: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[time_now] = mapped_column(nullable=False)
    updated_at: Mapped[update_time] = mapped_column(nullable=True)

    public_key: Mapped[bytes] = mapped_column(nullable=False)
    last_seen: Mapped[datetime] = mapped_column(nullable=False)
    is_online: Mapped[bool] = mapped_column(default=False)

    #relationship
    # sessions = relationship("Session", back_populates="user")