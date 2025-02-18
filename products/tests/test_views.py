from .fixtures import *
from users.tests.fixtures import *


def test_admin_can_create_product(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post('/api/v1/products/', {'sku': '67890', 'name': 'New Product', 'price': 20.00, 'brand': 'BrandX'})
    assert response.status_code == 201


def test_non_admin_cannot_create_product(api_client, normal_user):
    api_client.force_authenticate(user=normal_user)
    response = api_client.post('/api/v1/products/', {'sku': '99999', 'name': 'Forbidden', 'price': 30.00, 'brand': 'BrandY'})
    assert response.status_code == 403


def test_anonymous_can_list_products(api_client, product):
    response = api_client.get('/api/v1/products/')
    assert response.status_code == 200
    assert len(response.data) > 0


def test_query_count_increases(api_client, product):
    initial_count = product.query_count
    response = api_client.get(f'/api/v1/products/{product.id}/')
    product.refresh_from_db()
    assert response.status_code == 200
    assert product.query_count == initial_count + 1


def test_admin_can_update_product(api_client, admin_user, product):
    api_client.force_authenticate(user=admin_user)
    response = api_client.put(f'/api/v1/products/{product.id}/', {'sku': product.sku, 'name': 'Updated Name', 'price': 15.00, 'brand': 'UpdatedBrand'})
    assert response.status_code == 200


def test_non_admin_cannot_update_product(api_client, normal_user, product):
    api_client.force_authenticate(user=normal_user)
    response = api_client.put(f'/api/v1/products/{product.id}/', {'sku': product.sku, 'name': 'Hacker Name', 'price': 100.00, 'brand': 'HackedBrand'})
    assert response.status_code == 403


def test_admin_can_delete_product(api_client, admin_user, product):
    api_client.force_authenticate(user=admin_user)
    response = api_client.delete(f'/api/v1/products/{product.id}/')
    assert response.status_code == 204


def test_non_admin_cannot_delete_product(api_client, normal_user, product):
    api_client.force_authenticate(user=normal_user)
    response = api_client.delete(f'/api/v1/products/{product.id}/')
    assert response.status_code == 403