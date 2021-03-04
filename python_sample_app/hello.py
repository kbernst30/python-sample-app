from flask import Blueprint


hello_bp = Blueprint('hello', __name__, url_prefix='/')


@hello_bp.route('/')
def index() -> str:
    return "Hello World"
