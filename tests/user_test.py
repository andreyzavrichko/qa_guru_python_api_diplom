import allure

from api import requests
from data.user import user_first
from utils.schema import validate_json_schema


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User")
def test_create_user(base_url, delete_user):
    response = requests.post_request(base_url + '/user', json=user_first)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["type"] == "unknown", "type должен быть unknown"
    assert response.json()["message"], "message не может быть пустым"
    validate_json_schema("user/create_user.json", response)
    delete_user(user_first.get("username"))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with array")
def test_create_user_with_array(base_url, delete_user):
    payload = [user_first]
    response = requests.post_request(base_url + '/user/createWithArray', json=payload)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["type"] == "unknown", "type должен быть unknown"
    assert response.json()["message"], "ok"
    validate_json_schema("user/create_user.json", response)
    delete_user(user_first.get("username"))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Create User with list")
def test_create_user_with_list(base_url, delete_user):
    payload = [user_first]
    response = requests.post_request(base_url + '/user/createWithList', json=payload)
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["type"] == "unknown", "type должен быть unknown"
    assert response.json()["message"] == "ok", "message должен быть ok"
    validate_json_schema("user/create_user.json", response)
    delete_user(user_first.get("username"))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get User")
def test_get_user(base_url, create_user, delete_user):
    response = requests.get_request(base_url + f'/user/{user_first.get("username")}')
    assert response.status_code == 200, "Ожидается статус код 200"
    assert response.json()["username"] == user_first.get("username"), "username не совпадает"
    assert response.json()["firstName"] == user_first.get("firstName"), "firstName не совпадает"
    assert response.json()["email"] == user_first.get("email"), "email не совпадает"
    validate_json_schema("user/get_user.json", response)
    delete_user(user_first.get("username"))


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get not found User")
def test_get_not_found_user(base_url):
    response = requests.get_request(base_url + '/user/user55')
    assert response.status_code == 404, "Ожидается статус код 404"
    assert response.json()["type"] == "error", "type должен быть error"
    assert response.json()["message"] == "User not found", "message должен быть 'User not found'"
    validate_json_schema("user/user_not_found.json", response)


@allure.feature("User")
@allure.story("User")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Get empty User")
def test_get_empty_user(base_url):
    response = requests.get_request(base_url + '/user/')
    assert response.status_code == 405, "Ожидается статус код 405"
