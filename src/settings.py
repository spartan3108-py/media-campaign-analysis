from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    mongo_uri: str = "mongodb://localhost:27017"
    db_name: str = "dce-dev"

    class Config:
        env_file = ".env"


settings = Settings()
