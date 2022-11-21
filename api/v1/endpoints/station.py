from fastapi import APIRouter
from service import db
from schemas.station_schema import TaskBase
from schemas.station_task_schema import Task

router = APIRouter()


@router.get('/new_task/', response_model=TaskBase)
async def read_data_for_new_task() -> TaskBase:
    task = await db.read_data_for_new_task()
    result: TaskBase = TaskBase.from_orm(task)
    return result


@router.post('/add_coord', response_model=TaskBase)
async def add_task_to_db(task: Task) -> TaskBase:
    new_task = await db.add_task_to_db(task.latitude, task.longitude, task.priority)
    result: TaskBase = TaskBase.from_orm(new_task)
    return result
