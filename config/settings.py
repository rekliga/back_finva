import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    user: str
    host: str
    port: str
    bd_name: str
    password: str

    #claves para maps
    API_KEY:str
    BASE_URL:str
    class Config:
        env_file = ".env"


settings = Settings()
