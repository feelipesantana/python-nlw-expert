from flask import Blueprint,request, jsonify

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create-tag', methods=["POST"])
def create_tags():
    print(request.json)
    return jsonify({"resp": "ok"}), 200