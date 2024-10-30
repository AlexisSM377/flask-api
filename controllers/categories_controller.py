from models.category import Category
from models import db

def obtener_categorias():
    return Category.query.all()

def agregar_categoria(data):
    nueva_categoria = Category(categoryName=data['categoryName'], mainImage=data['mainImage'])
    db.session.add(nueva_categoria)
    db.session.commit()
    return "Categoría agregada correctamente"

def actualizar_categoria(id, data):
    categoria = Category.query.get(id)
    if categoria:
        categoria.categoryName = data['categoryName']
        categoria.mainImage = data['mainImage']
        db.session.commit()
        return "Categoría actualizada correctamente"
    else:
        return "Categoría no encontrada"

def eliminar_categoria(id):
    categoria = Category.query.get(id)
    if categoria:
        db.session.delete(categoria)
        db.session.commit()
        return "Categoría eliminada correctamente"
    else:
        return "Categoría ya no existe"