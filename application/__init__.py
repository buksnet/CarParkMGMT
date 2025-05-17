from flask import Flask, render_template
from flask_restx import Api, Resource
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from application.config import MAX_REQUESTS_PER_HR
from application.errors import default_limit_reach_responder

from application.models import Controller


class FixedAPI(Api):  # костыль, спасибо разрабам rest-x
    def render_root(self) -> str:
        return render_template('index.html')


app = Flask(__name__)
api = FixedAPI(app, doc='/swagger', version='1.0.0', contact='bukovskii.den@gmail.com')
app.config.from_object('application.config')
db_controller = Controller()
db_controller.create_all()

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
