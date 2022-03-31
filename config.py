import os

class Config:
    path_database = os.path.abspath("database.db")
    FLASK_ADMIN_SWATCH = 'flatly'
    DEBUG = True
    SECRET_KEY = 'kjfghjcghit78utfghj87t789i'
    BABEL_DEFAULT_LOCALE = 'pt'
    SQLALCHEMY_DATABASE_URI = r'sqlite:///' + path_database

class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '').replace("postgres", "postgresql")
