from flask import Blueprint, request, jsonify
from controllers.categories_controller import *

categories_routes = Blueprint('categories', __name__)

@categories_routes.route('/api/categories', methods=['GET'])
def get_categories():
    categories = obtener_categorias()
    categories_serializados = [{
        "id": c.id,
        "categoryName": c.categoryName,
        "mainImage": c.mainImage
    } for c in categories]
    return jsonify(categories_serializados)

@categories_routes.route('/api/categories', methods=['POST'])
def post_category():
    data = request.json
    mensaje = agregar_categoria(data)
    return jsonify({"mensaje": mensaje})

@categories_routes.route('/api/categories/<id>', methods=['PUT'])
def put_category(id):
    data = request.json
    mensaje = actualizar_categoria(id, data)
    return jsonify({"mensaje": mensaje})

@categories_routes.route('/api/categories/<id>', methods=['DELETE'])
def delete_category(id):
    mensaje = eliminar_categoria(id)
    return jsonify({"mensaje": mensaje})