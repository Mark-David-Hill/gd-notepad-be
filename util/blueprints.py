import routes

def register_blueprints(app):
    app.register_blueprint(routes.profiles)
    app.register_blueprint(routes.elements)
    app.register_blueprint(routes.users)
    app.register_blueprint(routes.notes)
    app.register_blueprint(routes.types)
    app.register_blueprint(routes.games)
    app.register_blueprint(routes.auth)
    app.register_blueprint(routes.tags)