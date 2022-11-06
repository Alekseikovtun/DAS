from fastapi import APIRouter
from service import db

router = APIRouter()


@router.get('/new_task/')
def read_data_for_new_task(
    user: str
):
    task = db.read_data_for_new_task(user)
    return task


@router.get('/add_coord')
def add_task_to_db(
    user: str,
    latitude: float,
    longitude: float,
    priority: str
):
    result = db.add_task_to_db(user, latitude, longitude, priority)
    return result
