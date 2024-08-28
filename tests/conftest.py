import pytest

from api import requests
from data.order import order_first


@pytest.fixture
def base_url():
    return 'https://petstore.swagger.io/v2'


@pytest.fixture
def create_order(base_url):
    response = requests.post_request(base_url + '/store/order', json=order_first)
    assert response.status_code == 200
    assert response.json()["id"], "Поле ID не должно быть пустым"
    order_id = response.json()["id"]
    return order_id
