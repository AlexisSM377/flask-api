from models import db

class Brand(db.Model):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    brandName = db.Column(db.String(100), nullable=False)
    logoBrand = db.Column(db.String(100), nullable=False)
    shoes = db.relationship('Shoe', backref='brand', lazy=True)

    def __repr__(self):
        return f'<Brand {self.brandName}>'