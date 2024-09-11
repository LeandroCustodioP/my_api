import os

class Config:
    SECRET_KEY = 'sua_chave_secreta'
    SQLALCHEMY_DATABASE_URI = 'postgresql://my_api_user:12345@localhost/my_api_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
