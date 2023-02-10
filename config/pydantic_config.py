from pydantic import BaseSettings


class Settings(BaseSettings):
    MYSQL_ROOT_PASSWORD: set
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DATABASE: str
    MYSQL_OUT_PORT: int
    MYSQL_HOST: str

settings = Settings()