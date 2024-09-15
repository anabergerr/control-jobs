from flask_restx import Api, Resource, fields, reqparse

api = Api()

job_schema = api.model('Job', {
    'id': fields.Integer(),
    'title': fields.String(),
    'type_job': fields.String(),
    'date': fields.Date(),
})