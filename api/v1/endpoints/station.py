from fastapi import APIRouter
from service import db

router = APIRouter()


@router.get('/new_task/')
def read_data_for_new_task():
    gps = db.read_data_for_new_task()
    return str(gps)


@router.get('/add_coord')
def add_coordinate_to_db(
    latitude: float,
    longitude: float
):
    db.add_coordinate_to_db(latitude, longitude)
    return str('Done')
