import os

from dotenv import load_dotenv
from pydantic import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Config(BaseSettings):
    """
    Base configuration
    """


class ProductionConfig(Config):
    """
    Production configuration
    """


class DevelopmentConfig(Config):
    """
    Development configuration
    """


class TestingConfig(Config):
    """
    Testing configuration
    """
    TESTING: bool = True
