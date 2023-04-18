from fastapi import APIRouter, Depends
from service import station
from schemas.station_schema import TaskBase, NewTaskFullReturn
from schemas.station_task_schema import Task, Cargo
from models.station import Task as ModelTask
from sqlalchemy.ext.asyncio import AsyncSession
from crud import get_db

router = APIRouter()


@router.get('/new_task/', response_model=NewTaskFullReturn)
async def read_data_for_new_task(
    battery: float,
    distance: float,
    weight: float, 
    volume: float,
    db: AsyncSession = Depends(get_db)
) -> NewTaskFullReturn:
    try:
        input_dict = dict(NewTaskFullReturn(input_battery = battery, input_distance = distance, input_weigth = weight, input_volume = volume))
        task_db: ModelTask = await station.read_data_for_new_task(db, distance, weight, volume)
        try:
            task: TaskBase = TaskBase.from_orm(task_db)
            input_dict["code"] = 200
            input_dict["msg"] = "OK"
            input_dict["item_geojson_type"] = "Feature"
            input_dict["item_geojson_geometry_type"] = "Point"
            input_dict["item_order_id"] = task.id
            input_dict["item_geojson_geometry_coordinates"] = [task.gps_latitude, task.gps_longitude]
            input_dict["item_geojson_properties_name"] = "Moscow"
            input_dict["total"] = 1
        except:
            input_dict["code"] = 200
            input_dict["msg"] = "OK"
            input_dict["total"] = 0
        result: NewTaskFullReturn = NewTaskFullReturn(**input_dict)
        return result
    except:
        except_response = {"code": 415, "msg": "Unsupported Media Type"}
        return except_response


@router.post('/add_new_task', response_model=Task)
async def add_task_to_db(
    task: Task,
    cargo: Cargo,
    db: AsyncSession = Depends(get_db)
) -> Task:
    try:
        new_task = await station.add_task_to_db(db, task.gps_latitude, task.gps_longitude, task.priority, task.task_status, cargo.weight, cargo.volume, cargo.name)
        result: Task = Task.from_orm(new_task)
        return result
    except:
        except_response = {"code": 415, "msg": "Unsupported Media Type"}
        return except_response
