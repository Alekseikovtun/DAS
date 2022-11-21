from crud import drone, station


async def read_data_for_new_task():
    resp = station.read_data_for_new_task()
    return resp

async def create_task_in_db(add_latitude, add_longitude, add_priority):
    resp = station.create_task_in_db(add_latitude, add_longitude, add_priority)
    return resp


async def create_drone_status(drone_id, battery, departure_lat, departure_long):
    await drone.create_drone_status(drone_id, battery, departure_lat, departure_long)


async def update_task_info(departure_lat, departure_long):
    resp = await station.update_task_info(departure_lat, departure_long)
    return resp
