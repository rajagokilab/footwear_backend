from django.contrib import admin
from django.urls import path, include
from .views import api_root, quit_view
from django.conf import settings
from django.conf.urls.static import static  # <-- import quit_view here
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', api_root),  # root URL returns JSON welcome message
    path('admin/', admin.site.urls),
    path('api/newsletter/', include('newsletter.urls')),
    path('Quit', quit_view),
    path('api/enquiry/', include('contacts.urls')),
    path('api/auth/', include('accounts.urls')),
    path('api/', include('products.urls')),
    path('api/orders/', include('orders.urls')),  
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),    # ← add this line

    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)