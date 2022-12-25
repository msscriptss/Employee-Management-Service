from app import api
from src.resources.employee import EmployeeHandler, EmployeesHandler, EmployeeStatsHandler
from src.routes.constants import Apis

api.add_resource(EmployeeHandler, Apis.EMPLOYEE_API)
api.add_resource(EmployeesHandler, Apis.EMPLOYEES_API)
api.add_resource(EmployeeStatsHandler, Apis.EMPLOYEE_STATS_API)

