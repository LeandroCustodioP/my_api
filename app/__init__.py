from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('configs.Config')

db.init_app(app)

# Importa as rotas da API
from app import routes


