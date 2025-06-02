from application.routes.data_models.index_models import get_total_model
from application.routes.index import index_api
from application.routes.controllers import index_controller
from flask_restx import Resource


@index_api.route('/get-vehicle-count')
@index_api.doc(description='Получение данных об общем числе транспортных средств')
class Vehicles(Resource):
    @index_api.marshal_with(get_total_model, description='Общее число и число активных транспортных средств')
    def get(self):
        """
        Получение общего и активного числа транспортных средств
        """
        return index_controller.get_vehicle_count(), 200


@index_api.route('/get-worker-count')
@index_api.doc(description='Получение данных об общем числе водителей на предприятии')
class Workers(Resource):
    @index_api.marshal_with(get_total_model, description='Общее число и число активных сотрудников')
    def get(self):
        """
        Получение общего и активного числа сотрудников
        """
        return index_controller.get_worker_count(), 200


@index_api.route('/get-driver-count')
@index_api.doc(description='Получение данных об общем числе водителей на предприятии')
class Drivers(Resource):
    @index_api.marshal_with(get_total_model, description='Общее число и число активных водителей')
    def get(self):
        """
        Получение общего и активного числа водителей
        """
        return index_controller.get_driver_count(), 200
