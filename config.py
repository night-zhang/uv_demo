from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    database_url: str = ""

    class Config:
        env_file = (".env", ".env.test", ".env.prod", ".env.local")
        extra = "allow"


cfg = Settings()

if __name__ == "__main__":
    print(f"Settings: {cfg.model_dump()}")
    print(f"cfg.model_dump().get('database_url'): {cfg.model_dump().get('database_url')}")
    print(f"DEBUG: {cfg.debug}")
    print(f"cfg.database_url: {cfg.database_url}")
    print(f"ENV_FILE: {cfg.Config.env_file}")
