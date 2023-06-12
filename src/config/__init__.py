from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    SECRET_KEY: str = Field(default="dfsdfs")




def config_instance():
    return Settings()
