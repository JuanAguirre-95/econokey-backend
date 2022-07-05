"""Configuration Objects"""


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevelopmentConfig(BaseConfig):
    """Development Config"""
    JWT_SECRET_KEY: str = "development"
    #SQLALCHEMY_DATABASE_URI: str = "sqlite:///database/econokey.db"


def get_config(scope: str):
    """
    Get the configuration class by scope name
    :param scope: Scope name
    :return: Config Class
    """
    if scope == "dev":
        return DevelopmentConfig
    return DevelopmentConfig
