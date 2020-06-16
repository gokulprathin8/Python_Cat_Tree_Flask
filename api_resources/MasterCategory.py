import json
from api_models.CategoryCreationModel import CategoryCreationModel
from flask_restful import Resource

class MasterCategory(Resource):
    def get(self):
        main_cat = []
        all_sub_cat = []
        sub_cat = CategoryCreationModel.get_sub_categories()
        for i in sub_cat:
            all_sub_cat.append(i.json())

        main_categories = CategoryCreationModel.get_main_categories()
        for i in main_categories:
            main_cat.append(i.json())

        for i in main_cat:
            i['children'] = []

        my_arr = []
        for i in all_sub_cat:
            for j in main_cat:
                if (i['childId'] == j['id']):
                    my_arr.append(i)
                    j['children'] = my_arr
        my_arr.clear()


        # for j in sub_cat:
        #     for i in main_cat:
        #         if (i['id'] == j['parentId']):
        #             print(i)

        if main_categories:
            return main_cat
        return {'message': 'no main categories found!'}