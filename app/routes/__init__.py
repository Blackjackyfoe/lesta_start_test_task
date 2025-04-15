from .ping import ping_bp
from .count import count_bp

def connect_routes(app):
    app.register_blueprint(ping_bp)
    app.register_blueprint(count_bp)