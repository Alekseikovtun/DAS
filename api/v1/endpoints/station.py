from fastapi import APIRouter
from service import db
from schemas.station_schema import TaskBase

router = APIRouter()


@router.get('/new_task/', response_model=TaskBase)
def read_data_for_new_task() -> TaskBase:
    task = db.read_data_for_new_task()
    result: TaskBase = TaskBase.from_orm(task)
    return result


@router.post('/add_coord', response_model=TaskBase)
def add_task_to_db(
    latitude: float,
    longitude: float,
    priority: str
) -> TaskBase:
    new_task = db.add_task_to_db(latitude, longitude, priority)
    result: TaskBase = TaskBase.from_orm(new_task)
    return result
