
from rest_framework.exceptions import ValidationError
from rest_framework.views import exception_handler, Response
from rest_framework import status

def handler(err: ValidationError, context: dict):
    response: Response = exception_handler(err, context)
    
    if response is None:
        return Response({
            'message': f'server error: {err}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR, exception=True)
        
    else:
        res = {'message': response.reason_phrase}
        res.update(response.data)
        return Response(res, status=response.status_code, exception=True)