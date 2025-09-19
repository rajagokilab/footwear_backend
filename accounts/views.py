from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from .serializers import RegisterSerializer

# ---------------- Register ----------------
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

# ---------------- Login ----------------
class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        # Check if user exists
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "User does not exist. Please register first."},
                status=404
            )

        # Authenticate user
        user_auth = authenticate(username=user.username, password=password)
        if user_auth is None:
            return Response({"error": "Incorrect password."}, status=400)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user_auth)
        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "username": user.username,
        })
