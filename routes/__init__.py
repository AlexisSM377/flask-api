from routes.shoes import shoes_routes
from routes.brands import brands_routes
from routes.categories import categories_routes

def init_routes(app):
    app.register_blueprint(shoes_routes)
    app.register_blueprint(brands_routes)
    app.register_blueprint(categories_routes)