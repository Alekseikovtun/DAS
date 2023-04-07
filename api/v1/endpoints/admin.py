from fastapi import APIRouter, Depends
from crud import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.admin_schema import MainTaskInfo, TaskStatus, UnrealStatus, SetUnrealStatus
from models.station import Task as ModelTask
from service import admin
from typing import List

router = APIRouter()

@router.post('/completed_tasks/', response_model=List[MainTaskInfo])
async def read_task_data(
    task_status: TaskStatus,
    db: AsyncSession = Depends(get_db)
) -> List[MainTaskInfo]:
    try:
        task_info: List[ModelTask] = await admin.read_task_data(db, task_status.task_status)
        result: List[MainTaskInfo] = [MainTaskInfo.from_orm(item) for item in task_info]
        return result
    except:
        except_response = {"code": 415, "msg": "Unsupported Media Type"}
        return except_response

@router.post('/set_task_status_unreal', response_model=UnrealStatus)
async def set_task_status_unreal(
    unreal_task_status: SetUnrealStatus,
    db: AsyncSession = Depends(get_db)
) -> UnrealStatus:
    try:
        result = await admin.set_task_status_unreal(db, unreal_task_status.task_id, unreal_task_status.task_status)
        return result
    except:
        except_response = {"code": 415, "msg": "Unsupported Media Type"}
        return except_response
