from flask import Blueprint, request, jsonify
from controllers.shoes_controller import *


shoes_routes = Blueprint('shoes', __name__)

@shoes_routes.route('/api/shoes', methods=['GET'])
def get_shoes():
    shoes = obtener_zapatos()
    shoes_serializados = [{
        "id": s.id,
        "productName": s.productName,
        "description": s.description,
        "imageShoes": s.imageShoes,
        "active": s.active,
        "price": s.price,
        "size": s.size,
        "stock": s.stock,
        "color": s.color,
        "isFeatured": s.isFeatured,
        "gender": s.gender
    } for s in shoes]
    return jsonify(shoes_serializados)

@shoes_routes.route('/api/shoes', methods=['POST'])
def post_shoe():
    data = request.json
    mensaje = agregar_zapato(data)
    return jsonify({"mensaje": mensaje})


@shoes_routes.route('/api/shoes/<id>', methods=['PUT'])
def put_shoe(id):
    data = request.json
    mensaje = actualizar_zapato(id, data)
    return jsonify({"mensaje": mensaje})

@shoes_routes.route('/api/shoes/<id>', methods=['DELETE'])
def delete_shoe(id):
    mensaje = eliminar_zapato(id)
    return jsonify({"mensaje": mensaje})
