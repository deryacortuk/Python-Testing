import requests
import json
import pytest

def test_load():

    url ="https://reqres.in/api/users?page=2"

    response =requests.get(url)   

    assert response.status_code == 200

def test_create():

    url ="https://reqres.in/api/users"    

    data = {
    "name": "morpheus",
    "job": "leader"
}
    response = requests.post(url,data=data)

    assert response.status_code == 201

def test_login():

    url = "https://reqres.in/api/login"   

    data = {
         "email": "peter@klaven"
    }

    response = requests.post(url,data=data)

    error = json.loads(response.text)

    
    assert response.status_code == 400
    assert error['error'] == "Missing password"

    


    


