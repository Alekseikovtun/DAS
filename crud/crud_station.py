from sqlalchemy import func, select
from models.station import Task, Cargo, Flight
from models.drone import Drone
from sqlalchemy.ext.asyncio import AsyncSession


class Station():
    async def read_data_for_new_task(self, db: AsyncSession) -> Task:
        q = select(func.min(Task.id))
        q = q.filter(Task.task_status == "NEW")
        resp = await db.execute(q)
        min_id = resp.scalar()
        q2 = select(Task).filter(Task.id == min_id)
        resp = await db.execute(q2)
        next_task: Task = resp.first()[0]
        
        update_task_status = next_task
        update_task_status.task_status = "OFFERING"        
        return next_task


    async def create_task_in_db(self, db: AsyncSession, add_gps_latitude, add_gps_longitude, add_priority, add_task_status, add_weight, add_volume, add_name):
        try:
            resp_cargo = await db.execute(func.max(Cargo.id))
            last_cargo = resp_cargo.first()[0]
            new_cargo = Cargo(
                id=last_cargo + 1,
                weight=add_weight,
                volume=add_volume,
                name=add_name,
            )
            resp_task = await db.execute(func.max(Task.id))
            last_task_id = resp_task.first()[0]
            new_task = Task(
                id=last_task_id+1,
                gps_latitude=add_gps_latitude,
                gps_longitude=add_gps_longitude,
                task_status=add_task_status,
                priority=add_priority,
                id_cargo=last_cargo + 1
            )
            db.add_all([new_cargo, new_task])
            return new_task
        except:
            new_cargo = Cargo(
                id=1,
                weight=add_weight,
                volume=add_volume,
                name=add_name,
            )
            new_task = Task(
                id = 1,
                gps_latitude=add_gps_latitude,
                gps_longitude=add_gps_longitude,
                task_status=add_task_status,
                priority=add_priority,
                id_cargo=last_cargo + 1
            )
            db.add_all([new_cargo, new_task])
            return new_task



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
    
    async def registration(self, login, password):
        login = login
        password = password
        refresh_token = "some kind of refresh_token"
        active_token = "some king of active_token"
        code = 200
        msg = "Tokens sent"
        coord_latitude = 0
        coord_longitude = 0
        drone_id = 1 #потом попроавить и сделать черех запрос
        dict = {
            "refresh_token":refresh_token,
            "active_token": active_token,
            "code": code,
            "msg": msg, 
            "coord_latitude": coord_latitude,
            "coord_longitude": coord_longitude,
            "drone_id":drone_id
        }
        return dict
    
    async def token_check(self, active_token):
        active_token = active_token
        code = 401
        msg = "Token Expired"
        dict = {
            "code": code,
            "msg": msg
        }
        return dict
    
    async def auth(self, login, refresh_token):
        login = login
        refresh_token = refresh_token
        active_token = "some king of active_token"
        code = 200
        msg = "Ok"
        dict = {
            "active_token": active_token,
            "code": code,
            "msg": msg
        }
        return dict

    async def acc_rej_task(self, db: AsyncSession, drone_id, status_code, task_id):
        q = select(Task).filter(
            Task.id == task_id
        )
        resp = await db.execute(q)
        record: Task = resp.first()[0]

        q1 = select(Drone).filter(
            Drone.id == drone_id
        )
        resp1 = await db.execute(q1)
        record1: Drone = resp1.first()[0]

        if status_code == True:
            record.task_status = "IN PROGRESS"
            record.id_drone = drone_id
            record1.drone_status = "FLYING"

            # dict = {}
            # dict["answer"] = "The drone took the task"
            # dict["task_id"] = task_id

            try:
                resp_flight = await db.execute(func.max(Flight.id))
                last_flight_id = resp_flight.first()[0]
                new_flight: Flight = Flight(
                    id=last_flight_id+1,
                    id_task=task_id,
                    flight_status="PROCESS"
                )
                db.add(new_flight)
            except:
                new_flight: Flight = Flight(
                    id=1,
                    id_task=task_id,
                    flight_status="PROCESS"
                )
                db.add(new_flight)
            # return dict
        else:
            record.task_status = "NEW"

            # dict = {}
            # dict["answer"] = "The drone refused the task"
            # dict["task_id"] = task_id
            # return dict

station = Station()