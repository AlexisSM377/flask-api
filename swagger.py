swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "Zapateria API",
        "description": "Documentación de la API para la gestión de zapatos",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http"
    ],
    "tags": [
        {
            "name": "Shoes",
            "description": "Operaciones relacionadas con zapatos"
        },
        {
            "name": "Brands",
            "description": "Operaciones relacionadas con marcas"
        },
        {
            "name": "Categories",
            "description": "Operaciones relacionadas con categorías"
        }
    ],
    "paths": {
        "/api/shoes": {
            "get": {
                "tags": ["Shoes"],
                "summary": "Obtener lista de zapatos",
                "description": "Devuelve una lista de todos los zapatos registrados",
                "responses": {
                    "200": {
                        "description": "Lista de zapatos",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Shoe"
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Shoes"],
                "summary": "Agregar un nuevo zapato",
                "description": "Agrega un nuevo zapato proporcionando los detalles necesarios",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Datos del zapato a agregar",
                        "schema": {
                            "$ref": "#/definitions/Shoe"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Zapato agregado correctamente"
                    }
                }
            }
        },
        "/api/shoes/{id}": {
            "put": {
                "tags": ["Shoes"],
                "summary": "Actualizar zapato",
                "description": "Actualiza un zapato existente basado en su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID del zapato a actualizar"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Datos actualizados del zapato",
                        "schema": {
                            "$ref": "#/definitions/Shoe"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Zapato actualizado correctamente"
                    },
                    "404": {
                        "description": "Zapato no encontrado"
                    }
                }
            },
            "delete": {
                "tags": ["Shoes"],
                "summary": "Eliminar zapato",
                "description": "Elimina un zapato existente basado en su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID del zapato a eliminar"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Zapato eliminado correctamente"
                    },
                    "404": {
                        "description": "Zapato no encontrado"
                    }
                }
            }
        },
        "/api/brands": {
            "get": {
                "tags": ["Brands"],
                "summary": "Obtener lista de marcas",
                "description": "Devuelve una lista de todas las marcas registradas",
                "responses": {
                    "200": {
                        "description": "Lista de marcas",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Brand"
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Brands"],
                "summary": "Agregar una nueva marca",
                "description": "Agrega una nueva marca proporcionando los detalles necesarios",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Datos de la marca a agregar",
                        "schema": {
                            "$ref": "#/definitions/Brand"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Marca agregada correctamente"
                    }
                }
            }
        },
        "/api/brands/{id}": {
            "put": {
                "tags": ["Brands"],
                "summary": "Actualizar marca",
                "description": "Actualiza una marca existente basada en su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID de la marca a actualizar"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Datos actualizados de la marca",
                        "schema": {
                            "$ref": "#/definitions/Brand"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Marca actualizada correctamente"
                    },
                    "404": {
                        "description": "Marca no encontrada"
                    }
                }
            },
            "delete": {
                "tags": ["Brands"],
                "summary": "Eliminar marca",
                "description": "Elimina una marca existente basada en su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID de la marca a eliminar"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Marca eliminada correctamente"
                    },
                    "404": {
                        "description": "Marca no encontrada"
                    }
                }
            }
        },
        "/api/categories": {
            "get": {
                "tags": ["Categories"],
                "summary": "Obtener lista de categorías",
                "description": "Devuelve una lista de todas las categorías registradas",
                "responses": {
                    "200": {
                        "description": "Lista de categorías",
                        "schema": {
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Category"
                            }
                        }
                    }
                }
            },
            "post": {
                "tags": ["Categories"],
                "summary": "Agregar una nueva categoría",
                "description": "Agrega una nueva categoría proporcionando los detalles necesarios",
                "parameters": [
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Datos de la categoría a agregar",
                        "schema": {
                            "$ref": "#/definitions/Category"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "Categoría agregada correctamente"
                    }
                }
            }
        },
        "/api/categories/{id}": {
            "put": {
                "tags": ["Categories"],
                "summary": "Actualizar categoría",
                "description": "Actualiza una categoría existente basada en su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID de la categoría a actualizar"
                    },
                    {
                        "in": "body",
                        "name": "body",
                        "description": "Datos actualizados de la categoría",
                        "schema": {
                            "$ref": "#/definitions/Category"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Categoría actualizada correctamente"
                    },
                    "404": {
                        "description": "Categoría no encontrada"
                    }
                }
            },
            "delete": {
                "tags": ["Categories"],
                "summary": "Eliminar categoría",
                "description": "Elimina una categoría existente basada en su ID",
                "parameters": [
                    {
                        "name": "id",
                        "in": "path",
                        "required": True,
                        "type": "integer",
                        "description": "ID de la categoría a eliminar"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Categoría eliminada correctamente"
                    },
                    "404": {
                        "description": "Categoría no encontrada"
                    }
                }
            }
        }
    },
    "definitions": {
        "Shoe": {
            "type": "object",
            "required": ["productName", "description", "imageShoes", "active", "price", "size", "stock", "color", "isFeatured"],
            "properties": {
                "id": {
                    "type": "integer"
                },
                "productName": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "imageShoes": {
                    "type": "string"
                },
                "active": {
                    "type": "boolean"
                },
                "price": {
                    "type": "number"
                },
                "size": {
                    "type": "string"
                },
                "stock": {
                    "type": "integer"
                },
                "color": {
                    "type": "string"
                },
                "isFeatured": {
                    "type": "boolean"
                },
                "gender": {
                    "type": "string"
                },
                "brand_id": {
                    "type": "integer"
                },
                "category_id": {
                    "type": "integer"
                }
            }
        },
        "Brand": {
            "type": "object",
            "required": ["brandName", "logoBrand"],
            "properties": {
                "id": {
                    "type": "integer"
                },
                "brandName": {
                    "type": "string"
                },
                "logoBrand": {
                    "type": "string"
                }
            }
        },
        "Category": {
            "type": "object",
            "required": ["categoryName", "mainImage"],
            "properties": {
                "id": {
                    "type": "integer"
                },
                "categoryName": {
                    "type": "string"
                },
                "mainImage": {
                    "type": "string"
                }
            }
        }
    }
}