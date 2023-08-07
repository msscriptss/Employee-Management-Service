from sqlalchemy import Column, String, Integer, func
from src.config import Base


class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(String)
    currency = Column(String)
    department = Column(String)
    sub_department = Column(String)

    @staticmethod
    def get_max(query):
        return func.max(query)

    @staticmethod
    def get_min(query):
        return func.min(query)

    @staticmethod
    def get_mean(query):
        return func.mean(query)
