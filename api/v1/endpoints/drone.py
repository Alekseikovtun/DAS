from fastapi import APIRouter
from service import db

router = APIRouter()


@router.get('/add_drone_info')
def add_dron_status(
    drone_id: int,
    battery: int,
    d_latitude: float,
    d_longitude: float
):
    db.add_dron_status(drone_id, battery, d_latitude, d_longitude)
    db.update_task_info(d_latitude, d_longitude)
    return str('Done')
