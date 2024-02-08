from flask import Blueprint,request, jsonify
from src.views.http_types.http_request import HttpRequest
from src.views.tg_creator_view import TagCreatorView
from src.errors.error_handler import handle_error
from src.validations.tag_create_validation import tag_create_validate

tags_routes_bp = Blueprint('tags_routes', __name__)

@tags_routes_bp.route('/create-tag', methods=["POST"])
def create_tags():
    response = None
    try:
        tag_create_validate(request)
        tag_creator_view = TagCreatorView()
        http_request = HttpRequest(body=request.json)
        response = tag_creator_view.validate_and_create(http_request)
        
    except Exception as exception:
        response = handle_error(exception)
        
    return jsonify(response.body), response.status_code