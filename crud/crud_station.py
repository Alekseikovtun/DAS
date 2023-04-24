from sqlalchemy import func, select
from models.station import Task, Cargo, Flight, DroneLoginData
from models.drone import Drone
from models.log import AllLogs
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import and_
from typing import List
from distance import distance as calculating_distance
import jwt


class Station():
    async def read_data_for_new_task(self, db: AsyncSession, distance, weight, volume) -> Task:
        q = select(Task).join(Cargo).filter(and_(Cargo.weight <= weight, Cargo.volume <= volume, Task.task_status == "NEW"))
        resp = await db.execute(q)
        all_new_tasks: List[Task] = resp.scalars().all()

        current_point_longitude = 55.110485
        current_point_latitude = 37.962350
        try:
            for row in all_new_tasks:
                dist_to_task_point = await calculating_distance(current_point_longitude,row.gps_latitude , current_point_latitude, row.gps_longitude)
                if dist_to_task_point <= distance:
                    found_new_task = row
                    found_new_task.task_status = "OFFERING"

                    new_log: AllLogs = AllLogs(
                        # id=last_log+1,
                        log_type="info",
                        context="The drone is offered a task"
                    )
                    db.add(new_log)
                    return found_new_task
        except:
            new_log: AllLogs = AllLogs(
                # id=last_log+1,
                log_type="info",
                context="There are no available tasks for the drone"
            )
            db.add(new_log)
            return None  

    async def create_task_in_db(self, db: AsyncSession, add_gps_latitude, add_gps_longitude, add_priority, add_task_status, add_weight, add_volume, add_name):
        try:
            resp_cargo = await db.execute(func.max(Cargo.id))
            last_cargo = resp_cargo.first()[0]
            new_cargo = Cargo(
                # id=last_cargo + 1,
                weight=add_weight,
                volume=add_volume,
                name=add_name,
            )
            # resp_task = await db.execute(func.max(Task.id))
            # last_task_id = resp_task.first()[0]
            new_task = Task(
                # id=last_task_id+1,
                gps_latitude=add_gps_latitude,
                gps_longitude=add_gps_longitude,
                task_status=add_task_status,
                priority=add_priority,
                id_cargo=last_cargo + 1
            )

            resp_log = await db.execute(func.max(AllLogs.id))
            last_log = resp_log.first()[0]
            new_log: AllLogs = AllLogs(
                id=last_log+1,
                log_type="info",
                context=f"Added a new task with cargo {add_name}"
            )
            db.add(new_log)
            db.add_all([new_cargo, new_task, new_log])
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

            new_log: AllLogs = AllLogs(
                log_type="info",
                context=f"Added a new task with ID {1} with cargo {add_name}"
            )
            db.add(new_log)
            db.add_all([new_cargo, new_task, new_log])
            return new_task


    async def registration(self, db: AsyncSession, login, password):
        encoded_refresh_token = jwt.encode({"refresh_token":"some kind of refresh_token"}, "DAS", algorithm="HS256")
        encoded_active_token = jwt.encode({"active_token":"some king of active_token"}, "DAS", algorithm="HS256")
        code = 200
        msg = "Tokens sent"
        coord_latitude = 37.962350
        coord_longitude = 55.110485
        resp_drone = await db.execute(func.max(Drone.id))
        last_drone = resp_drone.first()[0]

        new_drone_login_data: DroneLoginData = DroneLoginData(
            drone_id=last_drone,
            login=login,
            password=password,
            refresh_token=encoded_refresh_token,
            active_token=encoded_active_token
        )
        db.add_all([new_drone_login_data])

        dict = {
            "refresh_token":encoded_refresh_token,
            "active_token": encoded_active_token,
            "code": code,
            "msg": msg, 
            "coord_latitude": coord_latitude,
            "coord_longitude": coord_longitude,
            "drone_id":last_drone
        }
        return dict
    
    async def token_check(self, db: AsyncSession, login, refresh_token):
        q = select(DroneLoginData).filter(
            DroneLoginData.login == login,
            DroneLoginData.refresh_token == refresh_token
        )
        resp = await db.execute(q)
        record: DroneLoginData = resp.first()[0]

        dict = {
            "active_token": record.active_token,
            "code": 200,
            "msg": "A new token has been received"
        }
        return dict
    
    async def auth(self,  login, active_token, db: AsyncSession):
        q = select(DroneLoginData).filter(
            DroneLoginData.login == login
        )
        resp = await db.execute(q)
        record: DroneLoginData = resp.first()[0]


        if record.active_token == active_token:
            dict = {
                "code": 200,
                "msg": "Access is allowed"
            }
            return dict
        else:
            dict = {
                "code": 401,
                "msg": "Unauthorized"
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

            new_log: AllLogs = AllLogs(
                log_type="info",
                context=f"Drone number {drone_id} has accepted the task"
            )
            db.add(new_log)

            try:
                new_flight: Flight = Flight(
                    id_task=task_id,
                )
                db.add(new_flight)
            except:
                new_flight: Flight = Flight(
                    id=1,
                    id_task=task_id,
                )
                db.add(new_flight)
        else:
            record.task_status = "NEW"
            new_log: AllLogs = AllLogs(
                log_type="info",
                context=f"Drone number {drone_id} refused the task"
            )
            db.add(new_log)
    
    async def set_task_status_unreal(self, db: AsyncSession, task_id, task_status):
        q = select(Task).filter(
            Task.id == task_id
        )
        resp = await db.execute(q)
        record: Task = resp.first()[0]
        record.task_status = task_status

        record.task_status = "NEW"
        new_log: AllLogs = AllLogs(
            log_type="info",
            context=f"The administrator gave task number {task_id} the status {task_status}"
        )
        db.add(new_log)

        dict = {}
        dict["task_id"] = task_id
        dict["msg"] = "The new task status is set to Unreal"
        return dict

station = Station()
