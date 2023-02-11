from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    DB_USER: str = Field(..., env="DB_USER")
    DB_PASSWORD: str = Field(..., env="DB_PASSWORD")
    DB_NAME: str = Field(..., env="DB_NAME")
    DB_OUT_PORT: int = Field(..., env="DB_OUT_PORT")
    DB_HOST: str = "localhost"

    MYSQL_ROOT_PASSWORD: str = "something"
    MYSQL_USER: str = DB_USER
    MYSQL_PASSWORD: str = DB_PASSWORD
    MYSQL_DATABASE: str = DB_NAME
    MYSQL_OUT_PORT: int = DB_OUT_PORT
    MYSQL_HOST: str = DB_HOST

print("1")
settings = Settings()
print(settings.dict())
print("2")