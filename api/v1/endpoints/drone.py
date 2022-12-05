from fastapi import APIRouter, Depends
from service import drone
from schemas.station_schema import TaskBase
from schemas.drone_schema import Drone
from sqlalchemy.ext.asyncio import AsyncSession
from crud import get_db

router = APIRouter()


@router.post('/add_drone_info', response_model=TaskBase)
async def add_drone_status(
    drone_model: Drone,
    db: AsyncSession = Depends(get_db),
) -> TaskBase:
    await drone.add_drone_status(
        db, drone_model.drone_id, drone_model.battery, drone_model.d_latitude, drone_model.d_longitude
    )