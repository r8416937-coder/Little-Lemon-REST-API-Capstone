from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, MenuItemViewSet, BookingViewSet, RegistrationView, add_user_to_manager_group

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('menu-items', MenuItemViewSet, basename='menu-items')
router.register('bookings', BookingViewSet, basename='bookings')

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('groups/manager/users/', add_user_to_manager_group, name='add-manager'),
]
