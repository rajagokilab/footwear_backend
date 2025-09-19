from django.urls import path
from .views import product_list
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('products/', product_list, name='product-list'),
       path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)