from .fixtures import api_client, create_user, admin_user, normal_user



def test_create_user(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post('/api/v1/users/', {'username': 'newuser', 'password': 'testpass'})
    assert response.status_code == 201


def test_admin_can_create_users(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    response = api_client.post('/api/v1/users/', {'username': 'admin_created', 'password': 'pass', 'is_admin': True})
    assert response.status_code == 201


def test_non_admin_cannot_create_users(api_client, normal_user):
    api_client.force_authenticate(user=normal_user)
    response = api_client.post('/api/v1/users/', {'username': 'not_allowed', 'password': 'pass'})
    assert response.status_code == 403


def test_jwt_authentication(api_client, create_user):
    user = create_user(username='jwtuser', password='jwtpass')
    response = api_client.post('/api/token/', {'username': 'jwtuser', 'password': 'jwtpass'})
    assert 'access' in response.data

