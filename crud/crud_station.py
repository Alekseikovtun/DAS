from sqlalchemy import func, select
from models.station import Task
from sqlalchemy.ext.asyncio import AsyncSession


class Station():
    async def read_data_for_new_task(self, db: AsyncSession) -> Task:
        q = select(func.min(Task.id))
        q = q.filter(Task.task_status_id == 1)
        resp = await db.execute(q)
        min_id = resp.scalar()
        q2 = select(Task).filter(Task.id == min_id)
        resp = await db.execute(q2)
        next_task: Task = resp.first()[0]
        return next_task


    async def create_task_in_db(self, db: AsyncSession, add_gps_latitude, add_gps_longitude, add_priority, add_task_status) -> Task:
        try:
            resp = await db.execute(func.max(Task.id))
            last_coord_id = resp.first()[0]
            new_coord = Task(
                id=last_coord_id+1,
                gps_latitude=add_gps_latitude,
                gps_longitude=add_gps_longitude,
                task_status=add_task_status,
                priority=add_priority
            )
            db.add_all([new_coord])
            return new_coord
        except:
            new_coord = Task(
                id=1,
                gps_latitude=add_gps_latitude,
                gps_longitude=add_gps_longitude,
                task_status=add_task_status,
                priority=add_priority
            )
            db.add_all([new_coord])
            return new_coord



    async def update_task_info(self, db: AsyncSession, departure_lat, departure_long) -> Task:
        q = select(Task).filter(
            Task.latitude == departure_lat,
            Task.longitude == departure_long
        )
        resp = await db.execute(q)
        record: Task = resp.one()
        record.task_status_id = 3
        # db.commit()
        return record

station = Station()