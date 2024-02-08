from src.views.http_types.http_response import HttpResponse
from src.errors.error_type.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_error(error: Exception) -> HttpResponse: 
    
    if isinstance(error, HttpUnprocessableEntityError):
        return HttpResponse(status_code=error.status_code, 
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    
    return HttpResponse(status_code=500, body={
        "error":[{
            "title": "Server error",
            "detail": str(error)
        }]
    })