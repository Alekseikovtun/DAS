from crud import crud_drone, crud_station, crud_admin
from models.station import Task
from models.drone import Drone as ModelDrone
from typing import List


async def read_data_for_new_task(db, distance, weight, volume) -> Task:
    resp = await crud_station.station.read_data_for_new_task(db, distance, weight, volume)
    return resp

async def create_task_in_db(db, add_gps_latitude, add_gps_longitude, add_priority, add_task_status, add_weight, add_volume, add_name):
    resp = await crud_station.station.create_task_in_db(db, add_gps_latitude, add_gps_longitude, add_priority, add_task_status, add_weight, add_volume, add_name)
    return resp


async def add_new_drone(db, 
                        add_engine_power, 
                        add_flight_range, 
                        add_load_capacity, 
                        add_cargo_volume, 
                        add_battery_capacity
                        ) -> ModelDrone:
    return await crud_drone.drone.add_new_drone(db, add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity)


async def update_task_info(db, departure_lat, departure_long):
    resp = await crud_station.station.update_task_info(db, departure_lat, departure_long)
    return resp

async def read_task_data(db, task_status) -> List[Task]:
    resp = await crud_admin.admin.read_task_data(db, task_status)
    return resp

async def registration(login, password):
    resp = await crud_station.station.registration(login, password)
    return resp

async def token_check(active_token):
    resp = await crud_station.station.token_check(active_token)
    return resp

async def auth(login, refresh_token):
    resp = await crud_station.station.auth(login, refresh_token)
    return resp

async def acc_rej_task(db, drone_id, status_code, task_id):
    await crud_station.station.acc_rej_task(db, drone_id, status_code, task_id)
    # return resp

async def completed_task(db, drone_id, task_id, task_status):
    resp = await crud_drone.drone.completed_task(db, drone_id, task_id, task_status)
    return resp

async def set_task_status_unreal(db, task_id, task_status):
    resp = await crud_station.station.set_task_status_unreal(db, task_id, task_status)
    return resp
