from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="postgresql+asyncpg",
    username="postgres",
    password="password",
    host="localhost",
    database="fast_api_app",
    port=5432
)
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
AsyncSessionLocal = sessionmaker(
    bind=async_engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def get_async_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()