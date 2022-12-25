from app import api
from src.resources.users import UserHandler
from src.routes.constants import Apis


api.add_resource(UserHandler, Apis.USER_API)