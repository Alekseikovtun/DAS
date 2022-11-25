from crud import crud_drone, crud_station


async def read_data_for_new_task():
    resp = crud_station.station.read_data_for_new_task()
    return resp

async def create_task_in_db(add_latitude, add_longitude, add_priority):
    resp = crud_station.station.create_task_in_db(add_latitude, add_longitude, add_priority)
    return resp


async def create_drone_status(drone_id, battery, departure_lat, departure_long):
    await crud_drone.drone.create_drone_status(drone_id, battery, departure_lat, departure_long)


async def update_task_info(departure_lat, departure_long):
    resp = await crud_station.station.update_task_info(departure_lat, departure_long)
    return resp
