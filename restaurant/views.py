from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Category, MenuItem, Booking
from .serializers import CategorySerializer, MenuItemSerializer, BookingSerializer, UserRegistrationSerializer


def home(request):
    return render(request, 'restaurant/index.html')


class IsManagerOrAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        user = request.user
        return user and user.is_authenticated and (user.is_staff or user.groups.filter(name='Manager').exists())


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsManagerOrAdminOrReadOnly]


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManagerOrAdminOrReadOnly]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class RegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def add_user_to_manager_group(request):
    username = request.data.get('username')
    if not username:
        return Response({'detail': 'username is required'}, status=status.HTTP_400_BAD_REQUEST)
    user = User.objects.get(username=username)
    group, _ = Group.objects.get_or_create(name='Manager')
    user.groups.add(group)
    return Response({'detail': f'{username} added to Manager group'})
