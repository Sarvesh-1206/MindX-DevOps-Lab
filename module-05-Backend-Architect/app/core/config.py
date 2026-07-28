"""Application configuration loaded from environment variables."""

from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Validated application settings for the current environment."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "MindX DevOps Lab"
    environment: Literal[
        "development",
        "testing",
        "staging",
        "production",
    ] = "development"
    debug: bool = False
    database_url: str


settings = Settings()
