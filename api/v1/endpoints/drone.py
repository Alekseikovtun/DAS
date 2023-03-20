from fastapi import APIRouter, Depends
from service import drone
from schemas.drone_schema import Drone, DroneType 
from sqlalchemy.ext.asyncio import AsyncSession
from crud import get_db

router = APIRouter()


@router.post('/add_drone', response_model=Drone)
async def add_new_drone(
    drone_info: Drone,
    drone_type: DroneType,
    db: AsyncSession = Depends(get_db),
) -> Drone:
    new_drone = await drone.add_drone(
        db, drone_info.access_key, drone_info.drone_status, drone_info.place_number, drone_info.id_drone_type,
        drone_type.engine_power, drone_type.flight_range, drone_type.load_capacity, drone_type.cargo_volume, drone_type.battery_capacity
    )
    result: Drone = Drone.from_orm(new_drone)
    return result
