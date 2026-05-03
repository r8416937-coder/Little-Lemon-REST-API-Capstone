from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from restaurant import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include('restaurant.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
