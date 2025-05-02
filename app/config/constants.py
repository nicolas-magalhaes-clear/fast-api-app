from enum import Enum
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class DatabaseSettings(BaseSettings):
    DATABASE_URL: str


class CryptSettings(BaseSettings):
    SECRET_KEY: str


class EnvironmentOption(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class EnvironmentSettings(BaseSettings):
    ENVIRONMENT: EnvironmentOption = EnvironmentOption.DEVELOPMENT


class Constants(
    DatabaseSettings,
    CryptSettings,
    EnvironmentSettings,
):
    pass


constants = Constants()
