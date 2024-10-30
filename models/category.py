from models import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(100), nullable=False)
    mainImage = db.Column(db.String(100), nullable=False)
    shoes = db.relationship('Shoe', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.categoryName}>'