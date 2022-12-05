from models.station import Task
from service import db as db_serice

async def read_data_for_new_task(db) -> Task:
    return await db_serice.read_data_for_new_task(db)

async def add_task_to_db(db, add_latitude, add_longitude, add_priority):
    return await db_serice.create_task_in_db(db, add_latitude, add_longitude, add_priority)


async def update_task_info(db, departure_lat, departure_long):
    return await db_serice.update_task_info(db, departure_lat, departure_long)
