from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    TESTING: bool = False

    class Config:
        env_file = (".env", ".env.local", ".env.test", ".env.prod")

settings = Settings()