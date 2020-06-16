from db import db

class CategoryClosureModel(db.Model):
    __tablename__ ='category_closure_v2'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True, nullable=False)
    id_ancestor = db.Column(db.String(255), primary_key=False, nullable=False)
    id_descendant = db.Column(db.String(255), primary_key=False, nullable=False)

    def __init__(self, id_ancestor, id_descendant):
        self.id_ancestor = id_ancestor
        self.id_descendant = id_descendant

    def json(self):
        return{ 'id_ancestor': self.id_ancestor, 'id_descendant': self.id_descendant }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_tb(self):
        db.session.delete(self)
        db.session.commit()