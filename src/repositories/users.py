from src.config.config import DBConnection
from src.entities.users import Users as UsersModel
from src.entities.employees import Employees as EmployeeModel


class UserRepository:
    def insert_user(self, name, password):
        with DBConnection() as db:
            new_user = UsersModel(name=name, password=password)
            db.session.add(new_user)
            db.session.commit()