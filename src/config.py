# config.py at src level
#
# This file defines global configuration settings for your FastAPI application
# using Pydantic's BaseSettings for automatic environment variable loading.

from pydantic import Field
from typing import List, Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY")
    POSTGRES_STRING_URL: str = Field(..., env="POSTGRES_STRING_URL")
    REDIS_STRING_URL: str = Field(..., env="REDIS_STRING_URL")

    class Config:
        """Pydantic config for Settings."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"  # Ignore extra fields from .env


# Create a global settings object
settings = Settings()
