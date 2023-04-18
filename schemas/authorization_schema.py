from pydantic import BaseModel
from typing import Optional


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
    refresh_token: Optional[str]
    active_token: Optional[str]
    code: int
    msg: str
    coord_latitude: Optional[float]
    coord_longitude: Optional[float]
    drone_id: Optional[int]


class TestOutputInfo(BaseModel):
    code: int
    msg: str


class LogInOutputInfo(BaseModel):
    active_token: str
    code: int
    msg: str
