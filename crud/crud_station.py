from sqlalchemy import func, select
from models.station import Task
from sqlalchemy.ext.asyncio import AsyncSession


class Station():
    async def read_data_for_new_task(self, db: AsyncSession) -> Task:
        # resp = db.query(func.min(Task.id)).filter(
        #     Task.task_status_id == 1
        # ).scalar() 
        q = select(func.min(Task.id))
        q = q.filter(Task.task_status_id == 1)
        resp = await db.execute(q)
        min_id = resp.scalar()
        q2 = select(Task).filter(Task.id == min_id)
        resp = await db.execute(q2)
        next_task: Task = resp.all()[0]
        # next_task: Task = db.query(Task).filter(Task.id == resp).all()[0]
        return next_task


    async def create_task_in_db(self, db: AsyncSession, add_latitude, add_longitude, add_priority) -> Task:
        last_coord_id = db.query(func.max(Task.id)).scalar()
        new_coord = Task(
            id=last_coord_id+1,
            latitude=add_latitude,
            longitude=add_longitude,
            task_status_id=1,
            priority=add_priority
        )
        db.add_all([new_coord])
        db.commit()
        return new_coord


    async def update_task_info(self, db: AsyncSession, departure_lat, departure_long) -> Task:
        task_status_update = db.query(Task).filter(
            Task.latitude == departure_lat,
            Task.longitude == departure_long
        )
        record: Task = task_status_update.one()
        record.task_status_id = 3
        db.commit()
        return record

station = Station()