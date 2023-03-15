from fastapi import APIRouter, Depends
from service import station
from schemas.station_schema import TaskBase, NewTaskFullReturn, DroneInput, TaskGeoJSON
from schemas.station_task_schema import Task, Cargo
from models.station import Task as ModelTask
from sqlalchemy.ext.asyncio import AsyncSession
from crud import get_db

router = APIRouter()


@router.get('/new_task/', response_model=NewTaskFullReturn)
async def read_data_for_new_task(
    battery: int,
    distance: int,
    weight: int, 
    volume: int,
    db: AsyncSession = Depends(get_db)
) -> NewTaskFullReturn:
    input_dict = dict(DroneInput(battery = battery, distance = distance, weight = weight, volume = volume))
    task_db: ModelTask = await station.read_data_for_new_task(db)
    task: TaskBase = TaskBase.from_orm(task_db)
    geojson_dict = dict()
    geojson_dict["id"] = task.id
    # geojson_dict["geojson"] = {"type": "Feature", "geometry":{"type": "Point", "coordinates": [task.gps_latitude, task.gps_longitude]}, "properties": {"name": "Moscow"}}
    geojson_dict["geojson"] = {"geometry":{"coordinates": [task.gps_latitude, task.gps_longitude]}}
    geojson: TaskGeoJSON = TaskGeoJSON(**geojson_dict)
    result_dict = dict()
    result_dict["item"] = geojson
    result_dict["code"] = 200
    result_dict["msg"] = "OK"
    result_dict["droneinput"] = input_dict
    result: NewTaskFullReturn = NewTaskFullReturn(**result_dict)
    return result


@router.post('/add_new_task', response_model=Task)
async def add_task_to_db(
    task: Task,
    cargo: Cargo,
    db: AsyncSession = Depends(get_db)
) -> Task:
    new_task = await station.add_task_to_db(db, task.gps_latitude, task.gps_longitude, task.priority, task.task_status, cargo.weight, cargo.volume, cargo.name)
    result: Task = Task.from_orm(new_task)
    return result
