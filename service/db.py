from crud import crud_drone, crud_station, crud_admin
from models.station import Task
from models.drone import Drone as ModelDrone
from typing import List
from authorization import auth


async def read_data_for_new_task(
        login,
        active_token,
        db,
        db1,
        distance,
        weight,
        volume
) -> Task:
    auth_resp = await auth.auth.authorization(
        login,
        active_token,
        db
    )
    if auth_resp["code"] == 200:
        resp = await crud_station.station.read_data_for_new_task(
            db1,
            distance,
            weight,
            volume
        )
        return resp
    else:
        return auth_resp


async def create_task_in_db(
        db,
        add_gps_latitude,
        add_gps_longitude,
        add_task_status,
        add_weight,
        add_volume,
        add_name
):
    resp = await crud_station.station.create_task_in_db(
        db,
        add_gps_latitude,
        add_gps_longitude,
        add_task_status,
        add_weight,
        add_volume,
        add_name
    )
    return resp


async def add_new_drone(
        db,
        add_engine_power,
        add_flight_range,
        add_load_capacity,
        add_cargo_volume,
        add_battery_capacity
) -> ModelDrone:
    return await crud_drone.drone.add_new_drone(
        db,
        add_engine_power,
        add_flight_range,
        add_load_capacity,
        add_cargo_volume,
        add_battery_capacity
    )


async def update_task_info(
        db,
        departure_lat,
        departure_long
):
    resp = await crud_station.station.update_task_info(
        db,
        departure_lat,
        departure_long
    )
    return resp


async def read_task_data(
        db,
        task_status
) -> List[Task]:
    resp = await crud_admin.admin.read_task_data(
        db,
        task_status
    )
    return resp


async def registration(
        db,
        login,
        password
):
    resp = await auth.auth.registration(
        db,
        login,
        password
    )
    return resp


async def token_check(
        login,
        refresh_token
):
    resp = await auth.auth.token_check(
        login,
        refresh_token    
    )
    return resp


async def acc_rej_task(
        db,
        drone_id,
        status_code,
        task_id
):
    await crud_station.station.acc_rej_task(
        db,
        drone_id,
        status_code,
        task_id
    )


async def completed_task(
        db,
        drone_id,
        task_id,
        task_status,
        drone_log
):
    resp = await crud_drone.drone.completed_task(
        db,
        drone_id,
        task_id,
        task_status,
        drone_log
    )
    return resp


async def set_task_status_unreal(
        db,
        task_id,
        task_status
):
    resp = await crud_station.station.set_task_status_unreal(
        db,
        task_id,
        task_status
    )
    return resp
