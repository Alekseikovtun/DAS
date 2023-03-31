from pydantic import BaseModel

"""input"""
class SignInInputInfo(BaseModel):
    login: str
    password: str

class TestInputInfo(BaseModel):
    active_token: str

class LogInInputInfo(BaseModel):
    login: str
    refresh_token: str

"""output"""
class SingInOutputInfo(BaseModel):
    refresh_token: str
    active_token: str
    code: int
    msg: str
    coord_latitude: int
    coord_longitude: int
    drone_id: int

class TestOutputInfo(BaseModel):
    code: int
    msg: str

class LogInOutputInfo(BaseModel):
    active_token: str
    code: int
    msg: str
