import pytest
from products.models import Product


@pytest.fixture
def product(db):
    return Product.objects.create(sku='12345', name='Test Product', price=10.00, brand='TestBrand')