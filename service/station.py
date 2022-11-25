from service.db import (
    read_data_for_new_task, create_task_in_db, update_task_info
)

async def read_data_for_new_task():
    return await read_data_for_new_task()

async def add_task_to_db(add_latitude, add_longitude, add_priority):
    return await create_task_in_db(add_latitude, add_longitude, add_priority)


async def update_task_info(departure_lat, departure_long):
    return await update_task_info(departure_lat, departure_long)
