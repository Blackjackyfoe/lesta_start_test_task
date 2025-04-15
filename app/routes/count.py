from flask import Blueprint, jsonify, current_app

count_bp = Blueprint('count', __name__)

@count_bp.route('/count')
def count():
    current_app.redis.incr('counter')
    count_val = current_app.redis.get('counter')
    return jsonify({"count": int(count_val)})
