from typing import AsyncGenerator

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession, AsyncAttrs
from app.config import database_url


engine = create_async_engine(url=database_url)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession)

class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


class DatabaseSession:
    @staticmethod
    async def get_session(commit: bool = False) -> AsyncGenerator[AsyncSession, None]:
        async with async_session_maker() as session:
            try:
                yield session
                if commit:
                    await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()

    @staticmethod
    async def get_db() -> AsyncGenerator[AsyncSession, None]:
        async for session in DatabaseSession.get_session(commit=False):
            yield session

    @staticmethod
    async def get_db_with_commit() -> AsyncGenerator[AsyncSession, None]:
        async for session in DatabaseSession.get_session(commit=True):
            yield session

db = DatabaseSession()
