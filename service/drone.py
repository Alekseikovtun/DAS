from service.db import add_new_drone
from schemas.drone_schema import Drone as SchemaDrone
from models.drone import Drone as ModelDrone


async def add_drone(
        db, 
        add_engine_power, 
        add_flight_range, 
        add_load_capacity, 
        add_cargo_volume, 
        add_battery_capacity
        ) -> SchemaDrone:
    new_drone: ModelDrone = await add_new_drone(db, add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity)
    new_drone_schema: SchemaDrone = SchemaDrone.from_orm(new_drone)
    return new_drone_schema
    
