from flask import request
from flask_restful import Resource
from api_models.CategoryClosureModel import CategoryClosureModel

class CategoryClosureResource(Resource):
    def get(self):
        return {'cannot GET the request.'}

    def post(self):
        return {'message': 'message'}