import json

import allure

from utils.resource import path

import requests
from jsonschema.validators import validate


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

    schema = path('store/create_order.json')

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

    schema = path('store/inventory.json')

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

    schema = path('store/order.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))
