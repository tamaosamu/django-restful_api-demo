from django.http import JsonResponse

class ApiResponse(JsonResponse):
    def __init__(self, stacode = "0000", message = "success", **kwargs):
        result = {
            'stacode': stacode,
            'message': message,
            'data': None
        }
        if kwargs:
            result.update({"data": kwargs})
        return super().__init__(data=result)