import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    user: str
    host: str
    port: str
    bd_name: str
    password: str

    class Config:
        env_file = ".env"


settings = Settings()
