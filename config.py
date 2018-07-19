class Config(object):
    """
    Common configurations
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # USE_X_SENDFILE = True
    # Put any configurations here that are common across all environments
    APISPEC_TITLE = "Cloud Nest"
    APISPEC_SWAGGER_UI_URL = "/docs"
    APISPEC_VERSION = "v1"


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = False
    SITE_URL = 'http://localhost:5000'


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    SITE_URL = 'http://livingon.cloud'


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
