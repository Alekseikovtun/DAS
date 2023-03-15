from models.station import Task
from typing import List
from service import db as db_serice


async def read_task_data(db, task_status) -> List[Task]:
    return await db_serice.read_task_data(db, task_status)