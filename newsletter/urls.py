# newsletter/urls.py
from django.urls import path
from .views import subscribe, subscriber_count  # ✅ import both

urlpatterns = [
    path('subscribe/', subscribe, name='subscribe'),
    path('subscriber-count/', subscriber_count, name='subscriber_count'),  # ✅ your line here
]
