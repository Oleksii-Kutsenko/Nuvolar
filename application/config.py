from pydantic import BaseSettings


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
