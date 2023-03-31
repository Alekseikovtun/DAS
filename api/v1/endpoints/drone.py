from fastapi import APIRouter, Depends
from service import drone
from schemas.drone_schema import Drone, DroneType, DroneAndTypeFull, DroneSolution, DroneTaskCompletedAnswer, DroneTaskCompleted
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

@router.post('/acc_rej_task', response_model=None)
async def accepting_rejecting_task(
    drone_solution: DroneSolution,
    db: AsyncSession = Depends(get_db)
) -> None:
    await drone.accepting_rejecting_task(db,drone_solution.drone_id, drone_solution.status_code, drone_solution.task_id)
    

@router.post('/task_completed', response_model=DroneTaskCompletedAnswer)
async def drone_completed_task(
    flight_result: DroneTaskCompleted,
    db: AsyncSession = Depends(get_db)
) -> DroneTaskCompletedAnswer:
    result = await drone.drone_completed_task(db, flight_result.drone_id, flight_result.task_id, flight_result.task_status)
    return result
