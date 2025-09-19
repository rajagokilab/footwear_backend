# orders/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated


class OrderCreateView(APIView):
    permission_classes = [IsAuthenticated]  # 🔹 ensure user is logged in

    def post(self, request):
        data = request.data
        try:
            product = Product.objects.get(id=data['product'])
            
            # 🔹 associate order with logged-in user
            order = Order.objects.create(
                user=request.user,
                product=product,
                quantity=data['quantity'],
                total_price=data['total_price']
            )

            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
# orders/views.py
from rest_framework.permissions import IsAuthenticated

class TrackOrderView(APIView):
    permission_classes = [IsAuthenticated]  # require login

    def get(self, request):
        orders = Order.objects.filter(user=request.user).order_by('-created_at')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    # orders/views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer

class MyOrdersView(APIView):
    permission_classes = [IsAuthenticated]  # 🔹 must be authenticated

    def get(self, request):
        orders = Order.objects.filter(user=request.user)  # fetch only logged-in user's orders
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

