from datetime import datetime
from flask_limiter import RequestLimit
from dateutils import relativedelta
from flask import render_template, make_response, Response, url_for
from application.utils import to_relativedelta


# ------------------------------- Обработчики клиентских ошибок -------------------------------------
def default_limit_reach_responder(request_limit: RequestLimit) -> Response:
    reset_timestamp = datetime.fromtimestamp(request_limit.reset_at)

    time_left: relativedelta = to_relativedelta(reset_timestamp - datetime.now())
    rendered_time = f'{time_left.hours} часов {time_left.minutes} минут {time_left.seconds} секунд'
    return make_response(
        render_template('rate_limit.html', rendered_time=rendered_time),
        429
    )
