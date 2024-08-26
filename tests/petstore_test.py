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
def test_find_by_status(base_url):
    response = requests.get(base_url + '/v2/pet/9223372036854773000')
    assert response.status_code == 200
    assert response.json()["id"] == 9223372036854773000
    assert response.json()["name"] == "fish"

    schema = path('find_by_pet_id.json')

    with open(schema) as file:
        f = file.read()
        validate(response.json(), schema=json.loads(f))









####################################################################################

# def test_single_user(base_url):
#     id = 2
#     email = 'janet.weaver@reqres.in'
#     first_name = 'Janet'
#     last_name = 'Weaver'
#     response = requests.get(base_url + '/api/users/2')
#     assert response.status_code == 200
#     assert response.json()['data']['id'] == id
#     assert response.json()['data']['email'] == email
#     assert response.json()['data']['first_name'] == first_name
#     assert response.json()['data']['last_name'] == last_name
#     schema = path('single_user.json')
#
#     with open(schema) as file:
#         f = file.read()
#         validate(response.json(), schema=json.loads(f))
#
#
# def test_single_user_not_found(base_url):
#     response = requests.get(base_url + '/api/users/23')
#     assert response.status_code == 404
#     assert response.json() == {}
#
#
# def test_list_resource(base_url):
#     text = 'To keep ReqRes free, contributions towards server costs are appreciated!'
#     response = requests.get(base_url + '/api/unknown')
#     assert response.status_code == 200
#     assert response.json()['data'] != []
#     assert response.json()['total'] == 12
#     assert response.json()['support']['text'] == text
#
#     schema = path('list_resources.json')
#
#     with open(schema) as file:
#         f = file.read()
#         validate(response.json(), schema=json.loads(f))
#
#
# def test_single_resource(base_url):
#     data = {
#         "id": 2,
#         "name": "fuchsia rose",
#         "year": 2001,
#         "color": "#C74375",
#         "pantone_value": "17-2031"
#     }
#     response = requests.get(base_url + '/api/unknown/2')
#     assert response.status_code == 200
#     assert response.json()['data'] == data
#
#     schema = path('single_resources.json')
#
#     with open(schema) as file:
#         f = file.read()
#         validate(response.json(), schema=json.loads(f))
#
#
# def test_single_resource_not_found(base_url):
#     response = requests.get(base_url + '/api/unknown/23')
#     assert response.status_code == 404
#
#
# def test_login_successful(base_url):
#     payload = {
#         "email": "eve.holt@reqres.in",
#         "password": "cityslicka"
#     }
#     response = requests.post(base_url + '/api/login', data=payload)
#     assert response.status_code == 200
#     assert 'token' in response.json()
#     assert response.json()['token']
#
#     schema = path('login_successful.json')
#
#     with open(schema) as file:
#         f = file.read()
#         validate(response.json(), schema=json.loads(f))
#
#
# def test_login_unsuccessful(base_url):
#     payload = {
#         "email": "peter@klaven"
#     }
#     error = 'Missing password'
#     response = requests.post(base_url + '/api/login', data=payload)
#     assert response.status_code == 400
#     assert response.json()['error'] == error
#
#
# def test_register_successful(base_url):
#     payload = {
#         "email": "eve.holt@reqres.in",
#         "password": "pistol"
#     }
#     response = requests.post(base_url + '/api/register', data=payload)
#     assert response.status_code == 200
#     assert response.json()['id'] == 4
#     assert response.json()['token']
#
#
# def test_register_unsuccessful(base_url):
#     payload = {
#         "email": "sydney@fife"
#     }
#     error = 'Missing password'
#     response = requests.post(base_url + '/api/register', data=payload)
#     assert response.status_code == 400
#     assert response.json()['error'] == error
#
#
# def test_create(base_url):
#     payload = {
#         "name": "morpheus",
#         "job": "leader"
#     }
#     name = 'morpheus'
#     job = 'leader'
#     response = requests.post(base_url + '/api/users', data=payload)
#     assert response.status_code == 201
#     assert response.json()['name'] == name
#     assert response.json()['job'] == job
#     assert response.json()['id']
#
#
# def test_delete(base_url):
#     payload = {
#         "name": "morpheus",
#         "job": "leader"
#     }
#     response = requests.post(base_url + '/api/users', data=payload)
#     id = response.json()['id']
#     delete = requests.delete(base_url + '/api/users/' + id)
#     assert delete.status_code == 204
#
#
# def test_update(base_url):
#     payload_post = {
#         "name": "morpheus",
#         "job": "leader"
#     }
#     payload_update = {
#         "name": "morpheus",
#         "job": "zion resident"
#     }
#     new_job = 'zion resident'
#     response = requests.post(base_url + '/api/users', data=payload_post)
#     id = response.json()['id']
#     update = requests.put(base_url + '/api/users/' + id, data=payload_update)
#     assert update.status_code == 200
#     assert update.json()['job'] == new_job
#
#
# def test_patch(base_url):
#     payload_post = {
#         "name": "morpheus",
#         "job": "leader"
#     }
#     payload_update = {
#         "name": "morpheus",
#         "job": "zion resident"
#     }
#     new_job = 'zion resident'
#     response = requests.post(base_url + '/api/users', data=payload_post)
#     id = response.json()['id']
#     update = requests.patch(base_url + '/api/users/' + id, data=payload_update)
#     assert update.status_code == 200
#     assert update.json()['job'] == new_job

###########################################################################################





    #
    # @ Test
    # @ Feature("User")
    # @ Story("User")
    # @ DisplayName("Create User")
    # @ Severity(SeverityLevel.BLOCKER)
    # void createUserTest() {
    # User newUser = DataGenerator.getUser(8, 16, true, true, true);
    #
    # String response = given(Specs.request)
    # .body(newUser)
    # .when()
    # .post("/v2/user")
    # .then()
    # .spec(Specs.responseSpec)
    # .extract().path("message");
    #
    # assertThat(response).isEqualTo(newUser.getId().toString());
    # }
    #
    # @ Test
    # @ Feature("User")
    # @ Story("User")
    # @ DisplayName("Create User with array")
    # @ Severity(SeverityLevel.BLOCKER)
    # void createWithArrayTest() {
    # User newUser = DataGenerator.getUser(8, 16, true, true, true);
    #
    # String response = given(Specs.request)
    # .body(newUser)
    # .when()
    # .post("/v2/user/createWithArray")
    # .then()
    # .statusCode(500)
    # .extract().path("message");
    #
    # assertThat(response).isEqualTo("something bad happened");
    # }
    #
    # @ Test
    # @ Feature("User")
    # @ Story("User")
    # @ DisplayName("Create User with list")
    # @ Severity(SeverityLevel.BLOCKER)
    # void createWithListTest() {
    # User newUser = DataGenerator.getUser(8, 16, true, true, true);
    #
    # String response = given(Specs.request)
    # .body(newUser)
    # .when()
    # .post("/v2/user/createWithList")
    # .then()
    # .statusCode(500)
    # .extract().path("type");
    #
    # assertThat(response).isEqualTo("unknown");
    # }
    #
    # @ Test
    # @ Feature("User")
    # @ Story("User")
    # @ DisplayName("Get User")
    # @ Severity(SeverityLevel.CRITICAL)
    # void getUserTest() {
    # given(Specs.request)
    # .when()
    # .get("v2/user/user564564654")
    # .then()
    # .spec(Specs.responseSpec)
    # .body("id", is (4984564564654L));
    # }
    #
    # @ Test
    # @ Feature("User")
    # @ Story("User")
    # @ DisplayName("Get empty User")
    # @ Severity(SeverityLevel.TRIVIAL)
    # void getEmptyUserTest() {
    # given(Specs.request)
    # .when()
    # .get("v2/user/user55")
    # .then()
    # .statusCode(404)
    # .body("message", is ("User not found"));
    # }
    #
    # @ Test
    # @ Feature("User")
    # @ Story("User")
    # @ DisplayName("Get null User")
    # @ Severity(SeverityLevel.TRIVIAL)
    # void getNullUserTest() {
    # given(Specs.request)
    # .when()
    # .get("v2/user/")
    # .then()
    # .statusCode(405);
    # }
    #
    # @ Test
    # @ Feature("Order")
    # @ Story("Order")
    # @ DisplayName("Create Order")
    # @ Severity(SeverityLevel.NORMAL)
    # void createOrderTest() {
    # Order newOrder = DataGenerator.getOrder(8, 16, true, true, true);
    #
    # Integer response = given(Specs.request)
    # .body(newOrder)
    # .when()
    # .post("/v2/store/order")
    # .then()
    # .spec(Specs.responseSpec)
    # .extract().path("id");
    #
    # assertThat(response).isEqualTo(newOrder.getId());
    # }
    #
    # @ Test
    # @ Feature("Store")
    # @ Story("Store")
    # @ DisplayName("Check Inventory")
    # @ Severity(SeverityLevel.NORMAL)
    # void inventoryTest() {
    # given(Specs.request)
    # .when()
    # .get("/v2/store/inventory")
    # .then()
    # .spec(Specs.responseSpec)
    # .body("status", is (122));
    # }
    #
    # @ Test
    # @ Feature("Order")
    # @ Story("Order")
    # @ DisplayName("Find order")
    # @ Severity(SeverityLevel.CRITICAL)
    # void findOrderTest() {
    # given(Specs.request)
    # .when()
    # .get("/v2/store/order/2")
    # .then()
    # .statusCode(404)
    # .body("message", is ("Order not found"));
    # }
    #
    # @ Test
    # @ Feature("Pet")
    # @ Story("Pet")
    # @ DisplayName("Create pet")
    # @ Severity(SeverityLevel.BLOCKER)
    # void createPetTest() {
    # Pet newPet = DataGenerator.getPet(8, 16, true, true, true);
    #
    # Integer response = given(Specs.request)
    # .body(newPet)
    # .when()
    # .post("/v2/pet")
    # .then()
    # .spec(Specs.responseSpec)
    # .extract().path("id");
    #
    # assertThat(response).isEqualTo(newPet.getId());
    # }
