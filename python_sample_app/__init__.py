import os
from typing import Dict, Optional

from flask import Flask


def create_app(test_config: Optional[Dict] = None) -> Flask:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping()

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from .hello import hello_bp
    app.register_blueprint(hello_bp)

    return app
