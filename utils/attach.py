import json

import allure


def request_body(request_body_json):
    allure.attach(
        name='Request body',
        body=request_body_json,
        attachment_type=allure.attachment_type.JSON,
        extension='json'
    )


def response_body(response_body_json):
    allure.attach(
        name='Response body',
        body=json.dumps(response_body_json),
        attachment_type=allure.attachment_type.JSON,
        extension='json'
    )


def response_code(response_status_code):
    allure.attach(
        name='Response status code',
        body=response_status_code,
        attachment_type=allure.attachment_type.TEXT,
        extension='txt'
    )