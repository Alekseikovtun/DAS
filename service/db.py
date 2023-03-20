from crud import crud_drone, crud_station, crud_admin
from models.station import Task
from typing import List


async def read_data_for_new_task(db) -> Task:
    resp = await crud_station.station.read_data_for_new_task(db)
    return resp

async def create_task_in_db(db, add_gps_latitude, add_gps_longitude, add_priority, add_task_status, add_weight, add_volume, add_name):
    resp = await crud_station.station.create_task_in_db(db, add_gps_latitude, add_gps_longitude, add_priority, add_task_status, add_weight, add_volume, add_name)
    return resp


async def add_new_drone(db, add_access_key, add_drone_status, add_place_number, add_id_drone_type,
                        add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity
                        ):
    await crud_drone.drone.add_new_drone(db, add_access_key, add_drone_status, add_place_number, add_id_drone_type,
                                         add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity
                                         )


async def update_task_info(db, departure_lat, departure_long):
    resp = await crud_station.station.update_task_info(db, departure_lat, departure_long)
    return resp

async def read_task_data(db, task_status) -> List[Task]:
    resp = await crud_admin.admin.read_task_data(db, task_status)
    return resp
