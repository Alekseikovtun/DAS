import wrapt
from .crud_session import SessionLocal
from .crud_station import station
from .crud_drone import drone
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
