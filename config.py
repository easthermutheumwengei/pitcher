import os
class Config:
    '''
    General configuration parent class
    '''
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://esther:1234@localhost/pitcher'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}