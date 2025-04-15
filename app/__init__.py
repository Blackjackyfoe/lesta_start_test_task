from flask import Flask
from redis import Redis

def create_app():
    app = Flask(__name__)
    app.config.from_mapping({
        'REDIS_HOST': 'redis'
    })
    redis_host = app.config.get('REDIS_HOST', 'redis')
    app.redis = Redis(host=redis_host, port=6379, decode_responses=True)
    from app.routes import connect_routes
    connect_routes(app)
    return app
