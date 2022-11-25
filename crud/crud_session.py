from config import db_config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


connection_string = f"""postgresql://\
{db_config.POSTGRES_USER}:{db_config.POSTGRES_PASSWORD}\
@{db_config.POSTGRES_HOST}:{db_config.POSTGRES_OUT_PORT}/{db_config.POSTGRES_DB}"""


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