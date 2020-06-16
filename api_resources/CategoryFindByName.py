from flask import request
from flask_restful import Resource
from api_models.CategoryCreationModel import CategoryCreationModel

class CategoryFindByName(Resource):
    def get(self):
        req_name = request.args.get('name')
        item = CategoryCreationModel.find_by_name(req_name)
        if item:
            return item.json(), 200
        return {'message': 'not found!'}