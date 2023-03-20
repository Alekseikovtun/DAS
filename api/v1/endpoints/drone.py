from fastapi import APIRouter, Depends
from service import drone
from schemas.drone_schema import Drone, DroneType, DroneAndTypeFull
from sqlalchemy.ext.asyncio import AsyncSession
from crud import get_db

router = APIRouter()


@router.post('/add_drone', response_model=DroneAndTypeFull)
async def add_new_drone(
    drone_type: DroneType,
    db: AsyncSession = Depends(get_db),
) -> DroneAndTypeFull:
    new_drone: Drone = await drone.add_drone(
        db, drone_type.engine_power, drone_type.flight_range, drone_type.load_capacity, drone_type.cargo_volume, drone_type.battery_capacity
    )
    result = DroneAndTypeFull(drone_info=new_drone, drone_type=drone_type)
    return result
