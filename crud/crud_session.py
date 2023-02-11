from config import db_config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


connection_string = f"""mysql+asyncmy://\
{db_config.DB_USER}:{db_config.DB_PASSWORD}\
@{db_config.DB_HOST}:{db_config.DB_OUT_PORT}/{db_config.DB_NAME}"""

engine = create_async_engine(
    connection_string,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    echo=False
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)