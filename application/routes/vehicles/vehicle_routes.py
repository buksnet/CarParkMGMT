from flask import make_response, render_template

from application.routes.data_models.vehicle_models import *
from application.routes.vehicles import vehicle_api
from application.routes.controllers import vehicle_controller
from flask_restx import Resource


