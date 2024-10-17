from models.shoe import Brand
from models import db

def obtener_marcas():
    return Brand.query.all()

def agregar_marca(data):
    nueva_marca = Brand(brandName=data['brandName'], logoBrand=data['logoBrand'])
    db.session.add(nueva_marca)
    db.session.commit()
    return "Marca agregada correctamente"

def actualizar_marca(id, data):
    marca = Brand.query.get(id)
    if marca:
        marca.brandName = data['brandName']
        marca.logoBrand = data['logoBrand']
        db.session.commit()
        return "Marca actualizada correctamente"
    else:
        return "Marca no encontrada"

def eliminar_marca(id):
    marca = Brand.query.get(id)
    if marca:
        db.session.delete(marca)
        db.session.commit()
        return "Marca eliminada correctamente"
    else:
        return "Marca ya no existe"