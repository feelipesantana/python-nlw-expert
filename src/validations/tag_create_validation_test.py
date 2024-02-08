from .tag_create_validation import tag_create_validate

class MockRequest:
    def __init__(self,json) -> None:
        self.json = json
    
def test_create_validation(): 
    req = MockRequest(json={"product_code":"123"})
    tag_create_validate(req)