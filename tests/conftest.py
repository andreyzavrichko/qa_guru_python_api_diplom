import allure
import pytest

from api import requests
from data.order import order_first
from data.pet import pet_first


@pytest.fixture
def base_url():
    return 'https://petstore.swagger.io/v2'


@pytest.fixture
def create_order(base_url):
    with allure.step('Отправить запрос на создание заказа'):
        response = requests.post_request(base_url + '/store/order', json=order_first)
        assert response.status_code == 200
        assert response.json()["id"], "Поле ID не должно быть пустым"
        order_id = response.json()["id"]
        return order_id


@pytest.fixture
def create_pet(base_url):
    with allure.step('Отправить запрос на создание питомца'):
        response = requests.post_request(base_url + '/pet', json=pet_first)
        assert response.status_code == 200, "Ожидается статус код 200"
        pet_id = response.json()["id"]
        return pet_id


@pytest.fixture
def delete_pet(base_url):
    def _delete_pet(pet_id):
        with allure.step('Отправить запрос на удаление питомца'):
            response = requests.delete_request(base_url + f'/pet/{pet_id}')
            assert response.status_code == 200, "Ожидается статус код 200"

    yield _delete_pet

