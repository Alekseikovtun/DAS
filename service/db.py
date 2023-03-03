from crud import crud_drone, crud_station
from models.station import Task


async def read_data_for_new_task(db) -> Task:
    resp = await crud_station.station.read_data_for_new_task(db)
    return resp

async def create_task_in_db(db, add_gps_latitude, add_gps_longitude, add_priority, add_task_status):
    resp = await crud_station.station.create_task_in_db(db, add_gps_latitude, add_gps_longitude, add_priority, add_task_status)
    return resp


async def create_drone_status(db, drone_id, battery, departure_lat, departure_long):
    await crud_drone.drone.create_drone_status(db, drone_id, battery, departure_lat, departure_long)


async def update_task_info(db, departure_lat, departure_long):
    resp = await crud_station.station.update_task_info(db, departure_lat, departure_long)
    return resp
