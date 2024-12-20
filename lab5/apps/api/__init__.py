from flask import Blueprint
from flask_restx import Api
from .cars import ns as cars_ns


api_bp = Blueprint('api_bp', __name__, url_prefix='/api/v1')
authorizations = {"Bearer": {"type": "apiKey", "in": "header", "name": "Authorization"}}

api = Api(
    api_bp,
    title='Online-Cars',
    version='1.0',
    description='Rest API Online-Cars',
    authorizations=authorizations,
)

api.add_namespace(cars_ns, path="/cars")
