import jwt
from jwt.exceptions import ExpiredSignatureError
from jwt.api_jwt import PyJWT

from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from models.drone import Drone
from sqlalchemy import func, select
from config import auth_config

string = "123456"


class Auth():
    jwt = PyJWT()

    async def encode_tokens(self, login):
        args = {
            "scope": "active_token",
            "sub": login,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(seconds=60),
        }
        active_token = self.jwt.encode(payload=args, key=auth_config.KEY, algorithm=auth_config.ALGORITHMS)

        args1 = {
            "scope": "refresh_token",
            "sub": login,
            "iat": datetime.utcnow(),
        }
        refresh_token = self.jwt.encode(payload=args1, key=auth_config.KEY, algorithm=auth_config.ALGORITHMS)

        tokens = [active_token, refresh_token]
        return tokens

    async def encode_active_token(self, login):
        args = {
            "scope": "active_token",
            "sub": login,
            "iat": datetime.utcnow(),
            "exp": datetime.utcnow() + timedelta(seconds=60),
        }
        active_token = self.jwt.encode(payload=args, key=auth_config.KEY, algorithm=auth_config.ALGORITHMS)
        return active_token

    async def registration(self, db: AsyncSession, login, password):
        
        tokens = await self.encode_tokens(login)
        encoded_refresh_token = tokens[1]
        encoded_active_token = tokens[0]
        
        coord_latitude = 37.962350
        coord_longitude = 55.110485
        resp_drone = await db.execute(func.max(Drone.id))
        last_drone = resp_drone.first()[0]


        dict = {
            "refresh_token":encoded_refresh_token,
            "active_token": encoded_active_token,
            "code": 200,
            "msg": "The drone is registered", 
            "coord_latitude": coord_latitude,
            "coord_longitude": coord_longitude,
            "drone_id":last_drone
        }
        return dict
    
    async def authorization(self, login, active_token, db: AsyncSession):
        try:
            args = self.jwt.decode(jwt=active_token, key=auth_config.KEY, algorithm=auth_config.ALGORITHMS)
            if args['scope'] == "active_token":
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
        except ExpiredSignatureError:
            dict = {
                "code": 401,
                "msg": "Token expired"
                }
            return dict

    async def token_check(self, login, refresh_token):
        args = self.jwt.decode(jwt=refresh_token, key=auth_config.KEY, algorithm=auth_config.ALGORITHMS)
        if args['scope'] == "refresh_token":
            login = args["sub"]
            active_token = await self.encode_active_token(login=login)  
        dict = {
            "active_token": active_token,
            "code": 200,
            "msg": "A new token has been received"
        }
        return dict

auth = Auth()