from fastapi import APIRouter
from service import db

router = APIRouter()


@router.get('/add_drone_info')
def add_dron_status(
    user: str,
    drone_id: int,
    battery: int,
    d_latitude: float,
    d_longitude: float
):
    ds_result = db.add_dron_status(
        user, drone_id, battery, d_latitude, d_longitude)
    ut_result = db.update_task_info(d_latitude, d_longitude)
    return ds_result, ut_result
