from models.drone import Drone, DroneType
from models.station import Task, Flight
from models.log import AllLogs, DroneLog
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select


class Dronee():
    async def add_new_drone(self, db: AsyncSession, 
    add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity 
    ):
        try:
            q1 = select(DroneType).filter(DroneType.id == 1)
            q2 = select(DroneType).filter(DroneType.id == 2)
            q3 = select(DroneType).filter(DroneType.id == 3)

            resp_q1 = await db.execute(q1)
            full_q1: DroneType = resp_q1.first()[0]
            resp_q2 = await db.execute(q2)
            full_q2: DroneType = resp_q2.first()[0]
            resp_q3 = await db.execute(q3)
            full_q3: DroneType = resp_q3.first()[0]

            if full_q2.engine_power < add_engine_power < full_q3.engine_power or full_q2.flight_range < add_flight_range < full_q3.flight_range or full_q2.load_capacity < add_load_capacity < full_q3.load_capacity or full_q2.cargo_volume < add_cargo_volume < full_q3.cargo_volume or full_q2.battery_capacity < add_battery_capacity < full_q3.battery_capacity:
                new_drone_type_id = 3
            elif full_q1.engine_power < add_engine_power < full_q2.engine_power or full_q1.flight_range < add_flight_range < full_q2.flight_range or full_q1.load_capacity < add_load_capacity < full_q2.load_capacity or full_q1.cargo_volume < add_cargo_volume < full_q2.cargo_volume or full_q1.battery_capacity < add_battery_capacity < full_q2.battery_capacity:
                new_drone_type_id = 2
            else:
                new_drone_type_id = 1

            # resp_drone = await db.execute(func.max(Drone.id))            
            # last_drone = resp_drone.first()[0]

            resp_drone_place = await db.execute(func.max(Drone.place_number))            
            last_drone_place = resp_drone_place.first()[0]
            new_drone: Drone = Drone(
                # id=last_drone + 1,
                access_key="something",
                drone_status="FREE",
                place_number=last_drone_place + 1,
                # id_drone_type=add_id_drone_type
                id_drone_type=new_drone_type_id,
            )

            # resp_log = await db.execute(func.max(AllLogs.id))
            # last_log = resp_log.first()[0]
            new_log: AllLogs = AllLogs(
                # id=last_log+1,
                log_type="info",
                context=f'The drone has been created'
            )
            db.add_all([new_drone, new_log])
            return new_drone
        except Exception as ex:
            q1 = select(DroneType).filter(DroneType.id == 1)
            q2 = select(DroneType).filter(DroneType.id == 2)
            q3 = select(DroneType).filter(DroneType.id == 3)

            resp_q1 = await db.execute(q1)
            full_q1: DroneType = resp_q1.one()
            resp_q2 = await db.execute(q2)
            full_q2: DroneType = resp_q2.one()
            resp_q3 = await db.execute(q3)
            full_q3: DroneType = resp_q3.one()

            if full_q2.engine_power < add_engine_power < full_q3.engine_power or full_q2.flight_range < add_flight_range < full_q3.flight_range or full_q2.load_capacity < add_load_capacity < full_q3.load_capacity or full_q2.cargo_volume < add_cargo_volume < full_q3.cargo_volume or full_q2.battery_capacity < add_battery_capacity < full_q3.battery_capacity:
                new_drone_type_id = 3
            elif full_q1.engine_power < add_engine_power < full_q2.engine_power or full_q1.flight_range < add_flight_range < full_q2.flight_range or full_q1.load_capacity < add_load_capacity < full_q2.load_capacity or full_q1.cargo_volume < add_cargo_volume < full_q2.cargo_volume or full_q1.battery_capacity < add_battery_capacity < full_q2.battery_capacity:
                new_drone_type_id = 2
            else:
                new_drone_type_id = 1

            new_drone = Drone(
                # id=1,
                access_key="something",
                drone_status="FREE",
                place_number=1,
                # id_drone_type=add_id_drone_type,
                id_drone_type=new_drone_type_id,
            )

            # resp_log = await db.execute(func.max(AllLogs.id))
            # last_log = resp_log.first()[0]
            new_log: AllLogs = AllLogs(
                # id=last_log+1,
                log_type="info",
                context=f'The drone has been created'
            )
            db.add_all([new_drone, new_log])
            return new_drone

    async def completed_task(self, db: AsyncSession, drone_id, task_id, task_status, drone_log):
        q = select(Task).filter(
            Task.id == task_id
        )
        resp = await db.execute(q)
        record: Task = resp.first()[0]
        record.task_status = task_status
        record.completed_at = func.now()

        q1 = select(Drone).filter(
            Drone.id == drone_id
        )
        resp1 = await db.execute(q1)
        record1: Drone = resp1.first()[0]
        record1.drone_status = "FREE"

        q2 = select(Flight).filter(
            Flight.id_task == task_id
        )
        resp2 = await db.execute(q2)
        record2: Flight = resp2.first()[0]
        record2.finished_at = func.now()
        
        # resp_log = await db.execute(func.max(AllLogs.id))
        # last_log = resp_log.first()[0]
        new_log: AllLogs = AllLogs(
            # id=last_log+1,
            log_type="info",
            context=f'Task {task_id} completed with the status {task_status}'
        )
        db.add(new_log)

        # resp_log = await db.execute(func.max(AllLogs.id))
        # last_log = resp_log.first()[0]
        new_log: AllLogs = AllLogs(
            #id=last_log+1,
            log_type="drone_log",
            context=drone_log
        )
        db.add(new_log)

        # resp_drone_log = await db.execute(func)
        
        dict = {}
        dict["msg"] = "Task completed"
        dict["code"] = 200
        return dict
    
drone = Dronee()