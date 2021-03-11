from rest_framework import status
from rest_framework.response import Response


def exception_response(error):
    return Response(
        {
            'status': 403,
            'error': error.__str__()
        },
        status=status.HTTP_403_FORBIDDEN
    )


def fetch_data_response(data):
    """success response"""
    return Response(
        {
            'status': 200,
            'data': data,
            'message': 'fetch the data successfully'
        },
        status=status.HTTP_200_OK
    )


def not_found():
    return Response(
        {
            'status': 404,
            'message': 'failed',
            'error': "Shop not found"
        },
        status=status.HTTP_404_NOT_FOUND
    )
