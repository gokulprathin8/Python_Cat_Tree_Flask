from anytree import Node, RenderTree
from api_models.CategoryCreationModel import CategoryCreationModel

class Generate_Category_Tree():
    main_categories = CategoryCreationModel.get_main_categories()