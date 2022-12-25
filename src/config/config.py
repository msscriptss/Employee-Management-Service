# Core

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Libs
import os


class DBConnection:

    def __init__(self) -> None:
        self.__connection_string = f'sqlite:///database/testDB.db'
        self.session = None
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
        