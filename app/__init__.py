from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from instance.config import app_config

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    #app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    #Import for resources
    from app.resources.shoppinglist import ShoppingLists, ShoppingList

    #api.add_resource(ShoppingLists, '/api/v1/shoppinglists')
    api.add_resource(ShoppingList, '/api/v1/shoppinglist', '/api/v1/shoppinglist/<int:id>')



    return app
