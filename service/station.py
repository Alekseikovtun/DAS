from models.station import Task
from service import db as db_serice


async def read_data_for_new_task(
        db,
        distance,
        weight,
        volume
) -> Task:
    return await db_serice.read_data_for_new_task(
        db,
        distance,
        weight,
        volume
    )


async def add_task_to_db(
        db,
        add_gps_latitude,
        add_gps_longitude,
        add_priority,
        add_task_status,
        add_weight,
        add_volume,
        add_name
):
    return await db_serice.create_task_in_db(
        db, add_gps_latitude,
        add_gps_longitude,
        add_priority,
        add_task_status,
        add_weight,
        add_volume,
        add_name
    )


async def update_task_info(
        db,
        departure_lat,
        departure_long
):
    return await db_serice.update_task_info(
        db,
        departure_lat,
        departure_long
    )
