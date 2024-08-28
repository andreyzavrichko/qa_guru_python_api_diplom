import allure

from api import requests
from data.order import order_first
from utils.schema import validate_json_schema


@allure.feature("Order")
@allure.story("Order")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Create Order")
def test_create_order(base_url):
    response = requests.post_request(base_url + '/store/order', json=order_first)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["id"], "Поле ID не должно быть пустым"
    assert response.json()["petId"] == order_first.get("petId")
    assert response.json()["status"] == order_first.get("status")
    validate_json_schema("store/create_order.json", response)


@allure.feature("Store")
@allure.story("Store")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Check Inventory")
def test_check_inventory(base_url):
    response = requests.get_request(base_url + '/store/inventory')
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["sold"]
    assert response.json()["Available"]
    validate_json_schema("store/inventory.json", response)


@allure.feature("Order")
@allure.story("Order")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Find order")
def test_find_order(base_url):
    response = requests.get_request(base_url + '/store/order/8')
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["petId"] == 7
    assert response.json()["status"] == "placed"
    validate_json_schema("store/order.json", response)


@allure.feature("Order")
@allure.story("Order")
@allure.severity(allure.severity_level.NORMAL)
@allure.title("Delete Order")
def test_delete_order(base_url, create_order):
    order_id = create_order
    response = requests.delete_request(base_url + f'/store/order/{order_id}')
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["type"] == "unknown"
    assert response.json()["message"] == str(order_id)
    validate_json_schema("store/delete_order.json", response)
