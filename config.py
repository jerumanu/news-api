import os
class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=1dccc9e39b9a4448a93062453d502ee9'
    ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=1dccc9e39b9a4448a93062453d502ee9'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    @staticmethod
    def init_app(app):w
    pass
class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True
config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
