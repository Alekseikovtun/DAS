from fastapi import APIRouter, Depends
from crud import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.admin_schema import MainTaskInfo, TaskStatus
from models.station import Task as ModelTask
from service import admin
from schemas.station_task_schema import Task
from typing import List

router = APIRouter()

@router.post('/completed_tasks/', response_model=List[MainTaskInfo])
async def read_task_data(
    task_status: TaskStatus,
    db: AsyncSession = Depends(get_db)
) -> List[MainTaskInfo]:
    task_info: List[ModelTask] = await admin.read_task_data(db, task_status.task_status)
    result: List[MainTaskInfo] = [MainTaskInfo.from_orm(item) for item in task_info]
    return result
