from models.drone import Drone, DroneType
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func, select


class Dronee():
    async def add_new_drone(self, db: AsyncSession, add_access_key, add_drone_status, add_place_number, add_id_drone_type,
    add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity 
    ):
        try:
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

            resp_drone = await db.execute(func.max(Drone.id))            
            last_drone = resp_drone.first()[0]
            new_drone = Drone(
                id=last_drone + 1,
                access_key=add_access_key,
                drone_status=add_drone_status,
                place_number=add_place_number,
                # id_drone_type=add_id_drone_type
                id_drone_type=new_drone_type_id,
            )
            db.add_all([new_drone])
            return new_drone
        except:
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
                id=1,
                access_key=add_access_key,
                drone_status=add_drone_status,
                place_number=add_place_number,
                # id_drone_type=add_id_drone_type,
                id_drone_type=new_drone_type_id,
            )
            db.add_all([new_drone])
            return new_drone

drone = Dronee()