from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from .serializers import AdminUserSerializer
from users.permissions import IsAdmin


class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdmin]
    authentication_classes = [JWTAuthentication]