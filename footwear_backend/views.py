from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

@api_view(['GET'])
def api_root(request, format=None):
    """
    API Root – returns a JSON welcome message with available endpoints.
    """
    return Response({
        "message": "Welcome to StepUp Footwear API",
        "available_endpoints": {
            "Admin Panel": "/admin/",
            "Newsletter Subscription": "/api/newsletter/subscribe/",
            "Enquiry Submission": "/api/enquiry/submit/",
            "Products": "/api/products/",
            "Track My Orders": "/api/orders/my-orders/",
            "Login (JWT)": "/api/auth/login/",
            "Register (JWT)": "/api/auth/register/",
            "Refresh Token": "/refresh/"
        }
    })

@api_view(['GET'])
def quit_view(request):
    """
    Returns a simple goodbye message.
    """
    return Response({"message": "Goodbye from StepUp Footwear API!"}, status=status.HTTP_200_OK)
