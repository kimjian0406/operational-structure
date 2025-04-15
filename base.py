# app/configs/base.py

from pydantic_settings import BaseSettings

class Config(BaseSettings):
    SECRET_KEY: str = "default_secret_key"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "password123"
    MYSQL_DB: str = "fastapi_assignment"
    MYSQL_CONNECT_TIMEOUT: int = 5
    CONNECTION_POOL_MAXSIZE: int = 10

