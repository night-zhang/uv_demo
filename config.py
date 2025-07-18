from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    database_url: str = ""

    class Config:
        env_file = (".env", ".env.local", ".env.test", ".env.prod")
        extra = "allow"


cfg = Settings()

if __name__ == "__main__":
    print(f"DEBUG: {cfg.debug}")
    print(f"DEBUG: {cfg.database_url}")
    print(f"ENV_FILE: {cfg.Config.env_file}")
    print(f"Settings: {cfg.model_dump()}")
