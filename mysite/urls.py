from frontend import urls
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/', include('orders.urls')),
]
