from flask import make_response, render_template
from flask_restx import Resource

from application.routes.pages import pages_api


@pages_api.route('/vehicles')
@pages_api.doc(description='Получение данных об общем числе транспортных средств')
class VehiclePage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('vehicles.html'), 200,
                             headers)


@pages_api.route('/routes')
@pages_api.doc(description='Управление доступными маршрутами')
class RoutesPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('routes.html'), 200,
                             headers)


@pages_api.route('/employees')
@pages_api.doc(description='Управление сотрудниками')
class RoutesPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('employees.html'), 200,
                             headers)


@pages_api.route('/repairs')
@pages_api.doc(description='Получение данных о ремонтных работах над техникой')
class RoutesPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('repairs.html'), 200,
                             headers)


@pages_api.route('/garages')
@pages_api.doc(description='Управление гаражными хозяйствами')
class RoutesPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('garages.html'), 200,
                             headers)


@pages_api.route('/reports')
@pages_api.doc(description='Просмотр и создание отчётов от водителей')
class RoutesPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('reports.html'), 200,
                             headers)


@pages_api.route('/settings')
@pages_api.doc(description='Настройки приложения')
class RoutesPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('settings.html'), 200,
                             headers)
