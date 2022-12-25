# Core
from flask import Flask
from flask_restful import Api

# Libs
from dotenv import load_dotenv


# Config App
load_dotenv()
app = Flask(__name__)
api = Api(app)

from src.routes.user import *
from src.routes.employee import *
