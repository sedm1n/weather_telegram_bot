from types import 
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

class Base(AsyncAttrs, DeclarativeBase):
      pass

class User(Base):
      __tablename__ = 'Users'
      id: Mapped[int] = mapped_column(primary_key=True)
      user_telegram_id: Mapped[int] = mapped_column(unique=True, index=True)
      username: Mapped[str] = mapped_column(String(140), index=True)
      userfullname: Mapped[str] = mapped_column(String(140))
      
