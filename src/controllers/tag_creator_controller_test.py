from .tag_creator_controller import TagCreatorController

def test_create():
    mock_value = "image_path"
    tag_create_controller = TagCreatorController()
    
    result = tag_create_controller.create(mock_value)
    
    print(result)
    
    assert isinstance(result, dict)
    assert "data" in result
    assert "path" in result["data"]
    assert result["data"]["type"] == "Tag Image"
    