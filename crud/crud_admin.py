from sqlalchemy import func, select
from models.station import Task
from models.log import AllLogs
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

class Admin():
    
    async def read_task_data(self, db: AsyncSession, task_status) -> List[Task]:
        q = select(Task).filter(
            Task.task_status == task_status
        )
        resp = await db.execute(q)

        # resp_log = await db.execute(func.max(AllLogs.id))
        # last_log = resp_log.first()[0]
        new_log: AllLogs = AllLogs(
            # id=last_log+1,
            log_type="info",
            context=f'The administrator checked the tasks with the status {task_status}'
        )
        db.add(new_log)
        return resp.scalars().all()

admin = Admin()