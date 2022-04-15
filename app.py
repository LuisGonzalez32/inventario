from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.inventario import Inventario
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from utils.db import db

app = Flask(__name__)

app.config.from_object("config.BaseConfig")

SQLAlchemy(app)
Bcrypt(app)
Migrate(app, db)

app.register_blueprint(Inventario)
