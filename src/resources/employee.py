from flask import request
from flask_restful import Resource

from src.repositories.employees import EmployeeRepository
from src.resources.util import BaseAppView


class EmployeeHandler(Resource, BaseAppView):
    def delete(self, emp_id):
        employee_repo = EmployeeRepository()
        try:
            employee_repo.delete_employee(emp_id)
        except Exception as e:
            return self.return_error_response_with_status_code(e, status_code=500)
        return self.return_success_response_with_status_code({"resp": "success"})


class EmployeesHandler(Resource, BaseAppView):
    def post(self):
        data = request.get_json()
        employee_repo = EmployeeRepository()
        try:
            employee_repo.insert_employee(**data)
        except Exception as e:
            return self.return_error_response_with_status_code(e, status_code=500)
        return self.return_success_response_with_status_code({"resp": "success"})


class EmployeeStatsHandler(Resource, BaseAppView):
    def post(self):
        data = request.get_json()
        employee_repo = EmployeeRepository()
        try:
            stats = employee_repo.get_stats(data['filter_by'], data['group_by'])
        except Exception as e:
            return self.return_error_response_with_status_code(e, status_code=500)
        return self.return_success_response_with_status_code({"resp": "success", "stats": stats})

