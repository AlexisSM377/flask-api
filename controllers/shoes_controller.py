from models.shoe import Shoe
from models import db

def obtener_zapatos():
    return Shoe.query.all()

def agregar_zapato(data):
    nuevo_zapato = Shoe(productName= data['productName'], description= data['description'], imageShoes= data['imageShoes'], active= data['active'], price= data['price'], size= data['size'], stock= data['stock'], color= data['color'], isFeatured= data['isFeatured'], gender= data['gender'], brand_id= data['brand_id'], category_id= data['category_id'])
    db.session.add(nuevo_zapato)
    db.session.commit()
    return "Zapato agregado correctamente"

def actualizar_zapato(id, data):
    zapato = Shoe.query.get(id)
    if zapato:
        zapato.productName = data['productName']
        zapato.description = data['description']
        zapato.imageShoes = data['imageShoes']
        zapato.active = data['active']
        zapato.price = data['price']
        zapato.size = data['size']
        zapato.stock = data['stock']
        zapato.color = data['color']
        zapato.isFeatured = data['isFeatured']
        zapato.gener = data['gender']
        zapato.brand_id = data['brand_id']
        zapato.category_id = data['category_id']
        db.session.commit()
        return "Zapato actualizado correctamente"
    else:
        return "Zapato no encontrado"
    
def eliminar_zapato(id):
    zapato = Shoe.query.get(id)
    if zapato:
        db.session.delete(zapato)
        db.session.commit()
        return "Zapato eliminado correctamente"
    else:
        return "Zapato ya no existe"
    
