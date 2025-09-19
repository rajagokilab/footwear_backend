# newsletter/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubscriberSerializer
from .models import Subscriber
from django.core.mail import send_mail
from django.conf import settings

# POST: subscribe new email
@api_view(['POST'])
def subscribe(request):
    serializer = SubscriberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()  # Save to DB

        # Optional: send confirmation email to the subscriber
        send_mail(
            subject="Newsletter Subscription",
            message="Thank you for subscribing to StepUp Footwear!",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[serializer.data['email']],
            fail_silently=False,
        )

        return Response({"message": "Subscribed successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET: count of subscribers
@api_view(['GET'])
def subscriber_count(request):
    count = Subscriber.objects.count()
    return Response({'count': count})
