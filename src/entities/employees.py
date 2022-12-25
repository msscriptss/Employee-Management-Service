from sqlalchemy import Column, String, Integer
from src.config import Base


class Employees(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary = Column(String)
    currency = Column(String)
    department = Column(String)
    sub_department = Column(String)