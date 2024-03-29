from typing import Any, AsyncGenerator
import wrapt
from sqlalchemy.ext.asyncio import AsyncSession
from .crud_session import SessionLocal


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
        try:
            await session.commit()
        except Exception:
            await session.rollback()


@wrapt.decorator
async def rollback_db_on_error(
    wrapped: Any, instance: Any, args: list, kwargs: dict
) -> Any:
    session: AsyncSession = kwargs["db"]
    try:
        return await wrapped(*args, **kwargs)
    except Exception:
        await session.rollback()
    raise
