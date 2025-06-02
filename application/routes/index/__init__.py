from flask_restx.namespace import Namespace

index_api = Namespace('index_routes', 'Маршруты API для загрузки информации на главную страницу проекта', '/api/index')
