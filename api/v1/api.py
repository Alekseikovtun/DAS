from fastapi import APIRouter
from api.v1.endpoints import station, drone


api_router = APIRouter()


api_router.include_router(station.router, prefix='/station')
api_router.include_router(drone.router, prefix='/drone')
