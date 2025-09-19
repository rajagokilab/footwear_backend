# orders/urls.py
from django.urls import path
from .views import OrderCreateView, TrackOrderView  # ✅ import TrackOrderView

urlpatterns = [
    path('', OrderCreateView.as_view(), name='order-create'),  # POST /api/orders/
    path('my-orders/', TrackOrderView.as_view(), name='track-my-orders'),  # GET /api/orders/my-orders/
]
