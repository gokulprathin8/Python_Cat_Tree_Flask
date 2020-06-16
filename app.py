from flask import Flask
from flask_restful import Api, Resource
from db import db

from api_resources.CategoryResource import CategoryResource
from api_resources.CategoryClosureResource import CategoryClosureResource
from api_resources.CategoryFindByName import CategoryFindByName
from api_resources.JSONCategoryCvt import JSONCategoryCvt
from api_resources.JSONCategorySubCvt import JSONCategorySubCvt
from api_resources.MasterCategory import MasterCategory
from api_resources.SubCategoryCreate import SubCategoryCreate

app = Flask(__name__)
app.secret_key = 'CHANGE_SECRET_KEY_HERE'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1807@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(CategoryResource, '/addCategory')
api.add_resource(CategoryFindByName, '/categoryfindByName')
api.add_resource(JSONCategoryCvt, '/getMainCategory')
api.add_resource(JSONCategorySubCvt, '/getSubCategory')
api.add_resource(MasterCategory, '/masterCategory')
api.add_resource(SubCategoryCreate, '/subCategory')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
