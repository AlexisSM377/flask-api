from models import db

class Shoe(db.Model):
    __tablename__ = 'shoes'
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    imageShoes = db.Column(db.String(100), nullable=False)
    active = db.Column(db.Boolean, nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(100), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    color = db.Column(db.String(100), nullable=False)
    isFeatured = db.Column(db.Boolean, nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        return f'<Shoe {self.productName}>'
    
class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    brandName = db.Column(db.String(100), nullable=False)
    logoBrand = db.Column(db.String(100), nullable=False)
    shoes = db.relationship('Shoe', backref='brand', lazy=True)

    def __repr__(self):
        return f'<Brand {self.brandName}>'
    

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(100), nullable=False)
    mainImage = db.Column(db.String(100), nullable=False)
    shoes = db.relationship('Shoe', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.categoryName}>'
