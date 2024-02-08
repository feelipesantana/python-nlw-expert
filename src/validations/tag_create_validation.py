from cerberus import Validator
from src.errors.error_type.http_unprocessable_entity import HttpUnprocessableEntityError 

def tag_create_validate(request: any) -> None:
    body_validation = Validator({
        "product_code": {"type": "string", "required": True, "empty": False}
    })
    
    response= body_validation.validate(request.json)
    if response is False:
        raise HttpUnprocessableEntityError(body_validation.errors)