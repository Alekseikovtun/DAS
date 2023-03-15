from sqlalchemy import func, select
from models.station import Task
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

class Admin():
    
    async def read_task_data(self, db: AsyncSession, task_status) -> List[Task]:
        q = select(Task).filter(
            Task.task_status == task_status
        )
        resp = await db.execute(q)
        return resp.scalars().all()

admin = Admin()