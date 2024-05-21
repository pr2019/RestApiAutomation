import json
import pytest
from pprint import pprint as pp
import jsonpath
import requests


@pytest.fixture(scope="module")
def fixture_code():
    print("\nAPI test case started\n")
    print("----------------------------------")
    global fileLocation
    fileLocation = 'C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\CreateUser.json'
    yield
    print("\nAPI test case execution finished\n")
    print("\n----------------------------------\n")


@pytest.mark.P1
@pytest.mark.Sanity
@pytest.mark.Smoke
def test_001_create_new_user(fixture_code):
    # API URL
    url = "https://reqres.in/api/users"
    file = open(fileLocation, 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    # print(request_json)
    response = requests.post(url, request_json)
    # print(response.content)
    # print(response.status_code)
    assert response.status_code == 201, "data not uploaded"
    # Fetch Headers from response
    print(response.headers)
    # Fetch content from response
    print(response.content)
    print("-" * 200)
    # Fetch all headers data
    for k in response.headers:
        if k == "Content-Type":
            print(f"{k} = {response.headers[k]}")
        if k == "Content-Length":
            print(f"{k} = {response.headers[k]}")
        if k == "Connection":
            print(f"{k} = {response.headers[k]}")
        if k == "Server":
            print(f"{k} = {response.headers[k]}")

    # Parse response to Json Format
    json_response = json.loads(response.text)
    print("Json response")
    print(json_response)
    ID = jsonpath.jsonpath(json_response, 'id')
    assert ID[0] != 0


@pytest.mark.Smoke
@pytest.mark.Regression
def test_002_delete_user(fixture_code):
    # API URL
    url1 = "https://reqres.in/api/users?page=2"
    response = requests.delete(url1)
    print(response.status_code)
    assert response.status_code == 204, "Url not deleted"


@pytest.mark.Smoke
@pytest.mark.P2
def test_fetch_user_detail(fixture_code):
    # API URL
    url = "https://reqres.in/api/users?page=2"
    res = requests.get(url)
    print("State Code :", res.status_code)

    # Validate State Code
    assert res.status_code == 200, "request is not valid"

    # Fetch Response Header
    pp(res.headers)
    print(res.headers.get("Date"))
    print(res.headers.get("Content-Type"))
    print(res.headers.get("server"))

    # Fetch Cookies
    print(res.cookies)
    # Fetch encoding
    print(res.encoding)
    # Fetch Elapsed time
    print(res.elapsed)
    # Display Response content
    pp(res.content)
    # Parse response to Json format
    json_response = json.loads(res.text)
    print(json_response)
    # Fetch value using Json Path
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages)
    # Fetch all the data from the pages
    # data = jsonpath.jsonpath(json_response, 'data[0]')
    for i in range(0, 3):
        temp = jsonpath.jsonpath(json_response, 'data[' + str(i) + ']')
        if i < len(temp):
            for k in temp[i]:
                print(f"{k} -> {temp[i][k]}")


@pytest.mark.Smoke
@pytest.mark.P3
def test_004_get_headers(fixture_code):
    url = 'https://httpbin.org/get'

    headerdata = {"T1": 'First_Header', "T2": 'Second_Header'}

    param = {"name": 'Pradeep', "email": 'xyz@gmail.com', "number": '09328449023'}

    response = requests.get(url, headers=headerdata, params=param)

    # print(response.status_code)
    print(response.text)

    assert response.text != ""


@pytest.mark.P1
def test_update_source(fixture_code):
    # API URL
    url = "https://reqres.in/api/users/2"

    file = open(fileLocation, 'r')
    json_input = file.read()
    request_json = json.loads(json_input)

    response = requests.put(url, request_json)
    assert response.status_code == 200, "data not updated"

    response_json = json.loads(response.text)
    # print(response.text)
    # Parse response to json format
    content = jsonpath.jsonpath(response_json, 'content')
    print(content[0])

    updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
    print(updatedAt[0])

    assert updatedAt != ""
