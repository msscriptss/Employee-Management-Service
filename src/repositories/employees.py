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

    def get_stats(self):
        with DBConnection() as db:
            # TODO(): Implement it
            pass
