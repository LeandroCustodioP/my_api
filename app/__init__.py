from flask import Flask

app = Flask(__name__)
app.config.from_object('configs.Config')

# Importa as rotas da API
from app import routes


