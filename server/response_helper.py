# error response
def fail_response(message) -> dict:
    return {
        "success": False,
        "message": {
            "text": message,
        }
    }

def success_response(responses, message) -> dict:
    return {
        "success": True,
        "message": message,
        "data": responses
    }
