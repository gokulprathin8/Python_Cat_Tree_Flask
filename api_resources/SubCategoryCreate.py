import uuid
from flask_restful import Resource
from datetime import datetime
from flask import request
from api_models.CategoryCreationModel import CategoryCreationModel

class SubCategoryCreate(Resource):
    def get(self):
        item = CategoryCreationModel.get_sub_categories()
        if item:
            return item.json(), 200
        return {'message': 'nothing found!'}

    def post(self):
        now = datetime.now()
        req_id  = str(uuid.uuid4())
        req_name = request.args.get('name')
        req_slug = request.args.get('slug')
        req_cover_image = request.args.get('cover_image')
        req_background_image = request.args.get('background_image')
        req_icon = request.args.get('icon')
        req_category_title = request.args.get('category_title')
        req_description = request.args.get('description')
        req_meta_title = request.args.get('meta_title')
        req_meta_description = request.args.get('meta_description')
        req_parentId = str(uuid.uuid4())
        req_childId = request.args.get('childId')
        req_created_at = str(datetime.timestamp(now))
        req_updated_at = str(datetime.timestamp(now))
        req_category_label = request.args.get('category_label')
        req_is_main_category = request.args.get('is_mainCategory')
        item = CategoryCreationModel(id=req_id, name=req_name, slug=req_slug, cover_image=req_cover_image, background_image=req_background_image, icon=req_icon, category_title=req_category_title, description=req_description, meta_title=req_meta_title, meta_description=req_meta_description, created_at=req_created_at, updated_at=req_updated_at, parentId=req_parentId, childId=req_childId,category_label=req_category_label, is_mainCategory=req_is_main_category)
        item.save_to_db()

        return item.json(), 201

    def put(self):
        req_id = request.args.get('id')
        item = CategoryCreationModel.find_by_id(id=req_id)
        name = request.args.get('name')
        if item:
            item.name =  name
        else:
            return {'message': 'item not found!'}
        item.save_to_db()
        return item.json()


    def delete(self):
        req_id = request.args.get('id')
        item = CategoryCreationModel.find_by_id(id=req_id)
        if item:
            item.delete_from_db()
            return {'message': 'item deleted'}
        return {'message': 'item does not exist. Delete operation not performed'}
