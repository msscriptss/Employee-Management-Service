import json

from flask_restful import Resource

from src.resources.util import BaseAppView


class EmployeeHandler(Resource, BaseAppView):
    def delete(self, emp_id):
        print(emp_id)
        return self.return_success_response_with_status_code(json.dumps({"resp": "success"}))

    def get(self, emp_id):
        print(emp_id)
        return self.return_success_response_with_status_code(json.dumps({"resp": "success"}))

    def put(self, emp_id):
        print(emp_id)
        return self.return_success_response_with_status_code(json.dumps({"resp": "success"}))


class EmployeesHandler(Resource, BaseAppView):
    def post(self):
        print("Inside post")
        return self.return_success_response_with_status_code(json.dumps({"resp": "success"}))

    def get(self):
        # TODO(delete): post testing
        print("Inside get")
        return self.return_success_response_with_status_code(json.dumps({"resp": "success"}))


class EmployeeStatsHandler(Resource, BaseAppView):
    def get(self):
        return self.return_success_response_with_status_code(json.dumps({"resp": "success"}))

