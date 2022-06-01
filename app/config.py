"""Configuration Objects"""


class BaseConfig:
    JWT_SECRET_KEY: str = "Development"


class DevelopmentConfig(BaseConfig):
    """Development Config"""
    PARAMETER = 1


class ProductionConfig(BaseConfig):
    """Production Config"""
    pass


def get_config(scope: str):
    """
    Get the configuration class by scope name
    :param scope: Scope name
    :return: Config Class
    """
    if scope == "dev":
        return DevelopmentConfig
    return DevelopmentConfig
