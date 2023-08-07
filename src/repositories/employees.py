from src.config.config import DBConnection
from src.entities.employees import Employees as EmployeeModel


class EmployeeRepository:
    def insert_employee(self, name, salary, currency, department, sub_department):
        with DBConnection() as db:
            new_employee = EmployeeModel(name=name, salary=salary, currency=currency, department=department,
                                         sub_department=sub_department)
            db.session.add(new_employee)
            db.session.commit()

    def delete_employee(self, emp_id):
        with DBConnection() as db:
            EmployeeModel.query.filter_by(id=emp_id).delete()
            db.session.commit()

    def get_stats(self, filter_by, group_by):
        with DBConnection() as db:
            # TODO(): Implement it
            query = EmployeeModel.query
            if len(filter_by) > 0:
                query = query.filter_by(**filter_by)
            if len(group_by) > 0:
                query = query.filter_by(**group_by)
            _max = EmployeeModel.get_max(query)
            _min = EmployeeModel.get_min(query)
            mean = EmployeeModel.get_mean(query)
            return {"max": _max, "min": _min, "mean": mean}
