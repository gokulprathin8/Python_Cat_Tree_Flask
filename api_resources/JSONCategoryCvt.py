from api_models.CategoryCreationModel import CategoryCreationModel
from flask_restful import Resource

class JSONCategoryCvt(Resource):
    def get(self):
        main_cat = []
        main_categories = CategoryCreationModel.get_main_categories()
        for i in main_categories:
            main_cat.append(i.json())
        if main_categories:
            return main_cat
        return {'message': 'no main categories found!'}