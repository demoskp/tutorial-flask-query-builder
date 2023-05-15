from flask import Blueprint
from flask_restful import Api

from api.resources.user import UserList

blueprint = Blueprint("api", __name__, url_prefix="/api")
api = Api(blueprint, errors=blueprint.errorhandler)

api.add_resource(UserList, "/users")