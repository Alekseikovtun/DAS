from fastapi import APIRouter
from api.v1.endpoints import station, drone, admin
from api.v1.authorization import authorization


api_router = APIRouter()

"""station"""
api_router.include_router(station.router, prefix='/station')
api_router.include_router(drone.router, prefix='/drone')
api_router.include_router(admin.router, prefix='/admin')

"""authorization"""
api_router.include_router(authorization.router, prefix='/authorization')