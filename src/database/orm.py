

from .manager import async_session_factory, async_engine, Base


class AsyncORM:
    @staticmethod
    async def create_db():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod 
    async def drop_db():
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
    