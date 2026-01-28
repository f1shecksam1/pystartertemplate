from enum import Enum
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Environment(str, Enum):
    local = "local"
    staging = "staging"
    production = "production"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    project_name: str = "pystartertemplate"
    environment: Environment = Environment.local
    debug: bool = True

    log_level: str = "INFO"
    log_file_path: str = "logs/app.log"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
