from flask_restx import fields
from application.routes.index import index_api

get_total_model = index_api.model('TotalValuesModel', {
    'total_count': fields.Integer,
    'active': fields.Integer
})
