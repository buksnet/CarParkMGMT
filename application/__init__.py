from flask import Flask, render_template
from flask_restx import Api
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from application.config import MAX_REQUESTS_PER_HR
from application.errors import default_limit_reach_responder

from application.models import Controller

from application.routes.pages.pages_routes import pages_api
from application.routes.index.index_routes import index_api
from application.routes.vehicles.vehicle_routes import vehicle_api


# ------------------- Перегрузка корневого эндпоинта -------------------------
class FixedAPI(Api):
    def render_root(self) -> str:
        return render_template('index.html')


# ------------------- Инициализация переменных приложения -------------------
app = Flask(__name__)
api = FixedAPI(app, doc='/swagger', version='1.0.0', contact='bukovskii.den@gmail.com')
app.config.from_object('application.config')
app.jinja_env.auto_reload = True

# ------------------- Загрузка маршрутов API --------------------------------
api.add_namespace(index_api)
api.add_namespace(vehicle_api)
api.add_namespace(pages_api)

# ------------------- Инициализация ограничителя запросов -------------------
if not app.debug:
    limiter = Limiter(
        get_remote_address,
        app=app,
        storage_uri="memory://",
        on_breach=default_limit_reach_responder
    )
else:
    limiter = Limiter(
        get_remote_address,
        default_limits=[f"{MAX_REQUESTS_PER_HR} per hour"],
        app=app,
        storage_uri="memory://",
        on_breach=default_limit_reach_responder
    )
