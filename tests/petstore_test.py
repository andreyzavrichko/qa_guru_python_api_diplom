import json

import allure
import pytest

from utils.resource import path

import requests
from jsonschema.validators import validate


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Find by status")
@pytest.mark.parametrize("status", ["available", "pending", "sold", "null"])
def test_find_by_status(base_url, status):
    params = {"status": status}
    response = requests.get(base_url + '/v2/pet/findByStatus', params=params)
    assert response.status_code == 200
    data = response.json()
    for item in data:
        assert 'id' in item, f"Поле 'id' отсутствует в элементе: {item}"
        assert item['id'], f"Поле 'id' пустое в элементе: {item}"

    schema = path('find_by_status.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Find by pet ID")
def test_find_pet_by_id(base_url):
    response = requests.get(base_url + '/v2/pet/9223372036854775000')
    assert response.status_code == 200
    assert response.json()["id"] == 9223372036854775000
    assert response.json()["name"] == "doggie"

    schema = path('find_by_pet_id.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User")
def test_create_user(base_url):
    payload = {
        "username": "Andrey",
        "firstName": "Ivanov",
        "lastName": "string",
        "email": "test@test.ru",
        "password": "PassW0rd$",
        "phone": "11111111",
        "userStatus": 1
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post(base_url + '/v2/user', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "message не может быть пустым"

    schema = path('create_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with array")
def test_create_user_with_array(base_url):
    payload = [
        {
            "username": "Andrey",
            "firstName": "Ivanov",
            "lastName": "string",
            "email": "test@test.ru",
            "password": "PassW0rd$",
            "phone": "11111111",
            "userStatus": 1
        }
    ]
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post(base_url + '/v2/user/createWithArray', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "ok"

    schema = path('create_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with list")
def test_create_user_with_list(base_url):
    payload = [
        {
            "username": "Andrey",
            "firstName": "Ivanov",
            "lastName": "string",
            "email": "test@test.ru",
            "password": "PassW0rd$",
            "phone": "11111111",
            "userStatus": 1
        }
    ]
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post(base_url + '/v2/user/createWithList', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["type"] == "unknown"
    assert response.json()["message"], "ok"

    schema = path('create_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get User")
def test_get_user(base_url):
    response = requests.get(base_url + '/v2/user/Andrey')
    assert response.status_code == 200
    assert response.json()["username"] == "Andrey"
    assert response.json()["firstName"] == "Ivanov"
    assert response.json()["email"] == "test@test.ru"

    schema = path('get_user.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get not found User")
def test_get_not_found_user(base_url):
    response = requests.get(base_url + '/v2/user/user55')
    assert response.status_code == 404
    assert response.json()["type"] == "error"
    assert response.json()["message"] == "User not found"

    schema = path('user_not_found.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get empty User")
def test_get_empty_user(base_url):
    response = requests.get(base_url + '/v2/user/')
    assert response.status_code == 405


@allure.feature("Order")
@allure.story("Order")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Create Order")
def test_create_order(base_url):
    payload = {
        "petId": 55555,
        "quantity": 1,
        "shipDate": "2024-08-27T17:43:07.742Z",
        "status": "placed",
        "complete": True
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post(base_url + '/v2/store/order', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["id"], "Поле ID не должно быть пустым"
    assert response.json()["petId"] == 55555
    assert response.json()["status"] == "placed"

    schema = path('create_order.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("Store")
@allure.story("Store")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check Inventory")
def test_check_inventory(base_url):
    response = requests.get(base_url + '/v2/store/inventory')
    assert response.status_code == 200
    assert response.json()["sold"]
    assert response.json()["Available"]

    schema = path('inventory.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("Order")
@allure.story("Order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Find order")
def test_find_order(base_url):
    response = requests.get(base_url + '/v2/store/order/8')
    assert response.status_code == 200
    assert response.json()["petId"] == 7
    assert response.json()["status"] == "placed"

    schema = path('order.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))


@allure.feature("Pet")
@allure.story("Pet")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create pet")
def test_create_pet(base_url):
    payload = {
        "name": "pet",
        "status": "available"
    }
    headers = {
        "Content-Type": "application/json",
        "accept": "application/json"
    }
    response = requests.post(base_url + '/v2/pet', headers=headers, json=payload)
    assert response.status_code == 200
    assert response.json()["id"], "Поле ID не должно быть пустым"
    assert response.json()["name"] == "pet"
    assert response.json()["status"] == "available"

    schema = path('pet.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))
