from service import db


async def add_drone_status(drone_id, battery, departure_lat, departure_long):
    await db.create_drone_status(drone_id, battery, departure_lat, departure_long)