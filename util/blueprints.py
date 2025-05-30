import routes

def register_blueprints(app):
    app.register_blueprint(routes.relationships)
    app.register_blueprint(routes.color_schemes)
    app.register_blueprint(routes.items)
    app.register_blueprint(routes.users)
    app.register_blueprint(routes.notes)
    app.register_blueprint(routes.types)
    app.register_blueprint(routes.collections)
    app.register_blueprint(routes.auth)
    app.register_blueprint(routes.tags)