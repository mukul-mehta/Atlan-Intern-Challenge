import os

from logging import getLogger

from flask import current_app

from app import blueprint
from app import create_app, db
from app.logging_config import setup_logger


app = create_app()
app.register_blueprint(blueprint)

setup_logger()
LOG = getLogger(__name__)

if __name__ == "__main__":
    LOG.info("Running App")
    app.run(host = "127.0.0.1",
            port = 5000, debug=True)
