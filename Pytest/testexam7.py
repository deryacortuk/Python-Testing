import pytest
import requests
import json

@pytest.fixture
def con():
    return "https://reqres.in/"

def test_request(con):
    url = con + "api/login/"

    data = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
           }

    response = requests.post(url,data=data)

    token = json.loads(response.text)

    assert response.status_code == 200
    assert token['token'] ==  "QpwL5tke4Pnpja7X4"

