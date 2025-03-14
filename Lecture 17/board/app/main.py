from fastapi import FastAPI
from app.database import Base, engine
from app.router import router


app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    import asyncio

    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(create_tables())
