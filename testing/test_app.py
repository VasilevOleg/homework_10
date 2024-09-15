import pytest
from app import app

# Фикстура для создания тестового клиента Flask
@pytest.fixture
def test_client():
    # Устанавливаем приложение в тестовый режим
    app.config['TESTING'] = True
    # Создаем тестовый клиент
    with app.test_client() as client:
        yield client

# pylint: disable=redefined-outer-name
def test_index_route(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert '<h1>Welcome to the main page</h1>' in response.get_data(as_text=True)

# pylint: disable=redefined-outer-name
def test_about_route(test_client):
    response = test_client.get('/about/')
    assert response.status_code == 200
    assert '<h1>About</h1>' in response.get_data(as_text=True)
