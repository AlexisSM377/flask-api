from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from models.shoe import Shoe
from models.brand import Brand
from models.category import Category