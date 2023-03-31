from models.station import Task
from typing import List
from service import db as db_serice


async def read_task_data(db, task_status) -> List[Task]:
    return await db_serice.read_task_data(db, task_status)

async def set_task_status_unreal(db, task_id, task_status):
    return await db_serice.set_task_status_unreal(db, task_id, task_status)