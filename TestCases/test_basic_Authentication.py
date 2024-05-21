import requests
from requests.auth import HTTPBasicAuth


def test_with_authentication():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('pr2019', 'Github#2024'))
    print(response.text)
