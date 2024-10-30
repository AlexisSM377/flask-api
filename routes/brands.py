from flask import Blueprint, request, jsonify
from controllers.brands_controller import *

brands_routes = Blueprint('brands', __name__)

@brands_routes.route('/api/brands', methods=['GET'])
def get_brands():
    brands = obtener_marcas()
    brands_serializados = [{
        "id": b.id,
        "brandName": b.brandName,
        "logoBrand": b.logoBrand
    } for b in brands]
    return jsonify(brands_serializados)

@brands_routes.route('/api/brands', methods=['POST'])
def post_brand():
    data = request.json
    mensaje = agregar_marca(data)
    return jsonify({"mensaje": mensaje})

@brands_routes.route('/api/brands/<id>', methods=['PUT'])
def put_brand(id):
    data = request.json
    mensaje = actualizar_marca(id, data)
    return jsonify({"mensaje": mensaje})

@brands_routes.route('/api/brands/<id>', methods=['DELETE'])
def delete_brand(id):
    mensaje = eliminar_marca(id)
    return jsonify({"mensaje": mensaje})