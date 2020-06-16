from db import db

class CategoryCreationModel(db.Model):
    __tablename__ = 'category_v2'

    id = db.Column(db.String(255), primary_key=True, nullable=False)
    name = db.Column(db.String(255), primary_key=False, nullable=False)
    slug = db.Column(db.String(255), primary_key=False, nullable=False)
    cover_image = db.Column(db.String(2048), primary_key=False, nullable=False)
    background_image = db.Column(db.String(2048), primary_key=False, nullable=False)
    icon = db.Column(db.String(2048), primary_key=False, nullable=False)
    category_title = db.Column(db.String(255), primary_key=False, nullable=False)
    description = db.Column(db.String(255), primary_key=False, nullable=False)
    meta_title = db.Column(db.String(255), primary_key=False, nullable=False)
    meta_description = db.Column(db.String(255), primary_key=False, nullable=False)
    created_at = db.Column(db.String(255), primary_key=False, nullable=False)
    updated_at = db.Column(db.String(255), primary_key=False, nullable=False)
    parentId = db.Column(db.String(255), primary_key=False, nullable=False)
    childId = db.Column(db.String(255), primary_key=False, nullable=False)
    category_label = db.Column(db.String(255), primary_key=False, nullable=True)
    is_mainCategory = db.Column(db.String(5), primary_key=False, nullable=False)

    def __init__(self, id, name, slug, cover_image, background_image, icon, category_title, description, meta_title, meta_description, created_at, updated_at, parentId, category_label, is_mainCategory, childId):
        self.id = id
        self.name = name
        self.slug = slug
        self.cover_image = cover_image
        self.background_image = background_image
        self.icon = icon
        self.category_title = category_title
        self.description = description
        self.meta_title = meta_title
        self.meta_description = meta_description
        self.created_at = created_at
        self.parentId = parentId
        self.childId = childId
        self.category_label = category_label
        self.updated_at = updated_at
        self.is_mainCategory = is_mainCategory

    def json(self):
        return {'id': self.id,'name': self.name,'slug': self.slug,'cover_image': self.cover_image,'background_image': self.background_image,'icon': self.icon,'category_title': self.category_title,'description': self.category_title,'meta_title': self.meta_title,'meta_description': self.meta_description,'created_at': self.created_at,'parentId': self.parentId, 'childId': self.childId,'category_label': self.category_label, 'is_mainCategory': self.is_mainCategory}

    @classmethod
    def find_by_id(cls, id):
        return  cls.query.filter_by(id=id).first()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_parentId(cls, parentId):
        return cls.query.filter_by(parentId=parentId).first()

    @classmethod
    def find_by_category_title(cls, category_title):
        return cls.query.filter_by(category_title=category_title).first()

    @classmethod
    def get_all_categories(cls):
        return cls.query.filter().all()

    @classmethod
    def get_main_categories(cls):
        return cls.query.filter_by(is_mainCategory="True").all()

    @classmethod
    def get_sub_categories(cls):
        return cls.query.filter_by(is_mainCategory="False").all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()