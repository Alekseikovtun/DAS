from service.db import add_new_drone



async def add_drone(db, add_access_key, add_drone_status, add_place_number, add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity):
    await add_new_drone(db, add_access_key, add_drone_status, add_place_number, add_engine_power, add_flight_range, add_load_capacity, add_cargo_volume, add_battery_capacity)
    
