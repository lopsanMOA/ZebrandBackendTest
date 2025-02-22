from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import User
from .serializers import AdminUserSerializer
from users.permissions import IsAdmin
from drf_spectacular.utils import extend_schema, OpenApiResponse



@extend_schema(
        responses={
            200: OpenApiResponse(description='OK'),
            201: OpenApiResponse(description="Created"),
            204: OpenApiResponse(description="No Content"),
            400: OpenApiResponse(description='Bad Request'),
            401: OpenApiResponse(description="Unauthorized"),
            403: OpenApiResponse(description="Forbidden"),
            404: OpenApiResponse(description='Not Found'),
        },
    )
class AdminUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAdmin]
    authentication_classes = [JWTAuthentication]