from .tag_create_validation import tag_create_validate
from src.errors.error_type.http_unprocessable_entity import HttpUnprocessableEntityError

class MockRequest:
    def __init__(self,json) -> None:
        self.json = json
    
def test_create_validation(): 
    req = MockRequest(json={"product_code":"123"})
    tag_create_validate(req)
    
def  test_tag_create_validation_with_error():
    req = MockRequest(json={"product_code":123})
    
    try:
        tag_create_validate(req)
        assert False
    except Exception as exception   :
        assert isinstance(exception, HttpUnprocessableEntityError)