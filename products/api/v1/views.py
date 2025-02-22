from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from .serializers import ProductSerializer
from users.permissions import IsAdminOrReadOnly
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
        }
    )
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    authentication_classes = [JWTAuthentication]
    
    def retrieve(self, request, *args, **kwargs):
        product = self.get_object()
        product.query_count += 1
        product.save()
        return super().retrieve(request, *args, **kwargs)
