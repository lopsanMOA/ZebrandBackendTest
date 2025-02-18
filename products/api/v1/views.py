from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from products.models import Product
from .serializers import ProductSerializer
from users.permissions import IsAdminOrReadOnly


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
