from application.models.controllers import BaseController
from yaml import safe_load as yaml_load


class IndexController(BaseController):
    def __init__(self):
        super().__init__()
        with open('application/models/queries/index.yaml') as requests:
            self.fetch_requests = yaml_load(requests)['fetch']

    def get_vehicle_count(self) -> dict:
        total_vehicles = self.submit_query(
            self.fetch_requests['get_vehicle_count'],
            is_unitary=True
        )
        active_vehicles = self.submit_query(
            self.fetch_requests['get_active_vehicle_count'],
            is_unitary=True
        )

        result = {
            'total_count': int(total_vehicles[0]),
            'active': int(active_vehicles[0])
        }
        return result

    def get_worker_count(self) -> dict:
        total_workers = self.submit_query(
            self.fetch_requests['get_worker_count'],
            is_unitary=True
        )
        active_workers = self.submit_query(
            self.fetch_requests['get_active_worker_count'],
            is_unitary=True
        )

        result = {
            'total_count': int(total_workers[0]),
            'active': int(active_workers[0])
        }
        return result

    def get_driver_count(self) -> dict:
        total_drivers = self.submit_query(
            self.fetch_requests['get_driver_count'],
            is_unitary=True
        )
        active_drivers = self.submit_query(
            self.fetch_requests['get_active_driver_count'],
            is_unitary=True
        )

        result = {
            'total_count': int(total_drivers[0]),
            'active': int(active_drivers[0])
        }
        return result
