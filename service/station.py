from service import db


async def read_data_for_new_task():
    resp = await db.read_data_for_new_task()
    return resp

async def add_task_to_db(add_latitude, add_longitude, add_priority):
    resp = await db.create_task_in_db(add_latitude, add_longitude, add_priority)
    return resp


async def update_task_info(departure_lat, departure_long):
    resp = await db.update_task_info(departure_lat, departure_long)
    return resp
