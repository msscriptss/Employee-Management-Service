from flask import request
from flask_restful import Resource

from src.repositories.users import UserRepository
from src.resources.util import BaseAppView


class UserHandler(Resource, BaseAppView):
    def post(self):
        user_repo = UserRepository()
        user_repo.insert_user(request.json["name"], request.json["password"])
        return self.return_success_response_with_status_code({"resp": "success"})
