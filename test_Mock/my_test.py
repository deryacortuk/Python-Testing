
import requests


def get_data():
    return 'data'

def call_twitter():
    data = get_data()

    return data

def get_ip():
    response = requests.get("http://httpbin.org/ip")
    if response.status_code == 200:
        return response.json()['origin']
     
        
