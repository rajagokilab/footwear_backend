# contacts/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Enquiry
from .serializers import EnquirySerializer

@api_view(['POST'])
def submit_enquiry(request):
    """
    Accepts POST requests with name, email, phone, message.
    Stores data in DB and returns success message.
    """
    serializer = EnquirySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Enquiry submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
