from models.drone import DroneStatus
from sqlalchemy.ext.asyncio import AsyncSession


class Drone():
    async def create_drone_status(self, db: AsyncSession, drone_id, battery, departure_lat, departure_long):
        new_info = DroneStatus(
            id=drone_id,
            battery_charge_lvl=battery,
            departure_latitude=departure_lat,
            departure_longitude=departure_long
        )
        db.add_all([new_info])
        # db.commit()

drone = Drone()