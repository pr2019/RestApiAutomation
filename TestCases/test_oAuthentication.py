import requests
import json
import jsonpath


def test_oauth_api():
    token_url = "https://thetestingworldapi.com/Token"
    data = {'grant_type': 'password', 'username':'admin', 'password':'admin'}
    t_response = requests.post(token_url, data)
    print(t_response.text)
    API_URL = "https://thetestingworldapi.com/api/StDetails/{id}"
    response = requests.get(API_URL)
    print(response.text)
