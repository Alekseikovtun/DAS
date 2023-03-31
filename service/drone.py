from service.db import add_new_drone, acc_rej_task, completed_task
from schemas.drone_schema import Drone as SchemaDrone
from models.drone import Drone as ModelDrone


async def add_drone(
        db, 
        add_engine_power, 
        add_flight_range, 
        add_load_capacity, 
        add_cargo_volume, 
        add_battery_capacity
        ) -> SchemaDrone:
    new_drone: ModelDrone = await add_new_drone(db, add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity)
    new_drone_schema: SchemaDrone = SchemaDrone.from_orm(new_drone)
    return new_drone_schema

async def accepting_rejecting_task(
        db,
        drone_id,
        status_code,
        task_id
    ):
    await acc_rej_task(db, drone_id, status_code, task_id)
    

async def drone_completed_task(
        db, 
        drone_id,
        task_id,
        task_status
):
    resp = await completed_task(db, drone_id, task_id, task_status)
    return resp