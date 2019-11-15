import os

from logging import getLogger
from flask import Flask, Blueprint, render_template
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

from app.exampleCase1 import case1 
from app.exampleCase2 import case2
from app.exampleCase3 import case3

LOG = getLogger(__name__)
LOG.info("configured logger")

db = SQLAlchemy()

blueprint = Blueprint('api', __name__)

def create_app():
    """
    Creates the flask app that gives all other methods context
    """

    app = Flask(__name__)
    app.config.from_object(Config)
    LOG.info("App loaded with config")
    
    app.app_context().push()
    LOG.info("Application context pushed")

    app.register_blueprint(case1)
    app.register_blueprint(case2)
    app.register_blueprint(case3)

    @app.route('/')
    def index():
        return render_template("index.html")

    return app

