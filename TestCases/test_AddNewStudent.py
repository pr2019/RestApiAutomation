import requests
import jsonpath
import json
from .Library import Common
IDs = []


def test_add_student_data():
    global IDs
    # API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    #
    # f = "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\RequestJosn.json"
    # json_input = open(f, 'r')
    #
    # json_request = json.loads(json_input.read())
    obj = Common("https://thetestingworldapi.com/api/studentsDetails",
                 "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\RequestJosn.json")
    api_url, json_request = obj.common_steps()

    response = requests.post(api_url, json_request)
    assert response.status_code == 201

    # json_data = json.loads(response.text)
    json_data = response.json()
    Id = jsonpath.jsonpath(json_data, "id")
    IDs.append(Id[0])


def test_get_student_data():
    for ids in IDs:
        API_URL = "https://thetestingworldapi.com/api/studentsDetails/" + str(ids)
        response = requests.get(API_URL)
        # print(response.text)
        assert response.status_code == 200
        json_data = response.json()
        data = jsonpath.jsonpath(json_data, "data")
        assert data[0]['id'] == ids


def test_update_student_data():
    # API_URL = "https://thetestingworldapi.com/api/studentsDetails/" + str(IDs[0])
    #
    # f = "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\UpdateJosn.json"
    # json_input = open(f, 'r')
    #
    # json_request = json.loads(json_input.read())
    obj = Common("https://thetestingworldapi.com/api/studentsDetails/" + str(IDs[0]),
                 "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\UpdateJosn.json")
    api_url, json_request = obj.common_steps()
    json_request['id'] = IDs[0]
    # print(json_request)
    response = requests.put(api_url, json_request)
    # print(response.text)
    update_response = response.json()
    status = jsonpath.jsonpath(update_response, "status")
    msg = jsonpath.jsonpath(update_response, "msg")
    assert status[0] == 'true' and msg[0] == 'update  data success'
    # res = requests.get(API_URL)
    # print(res.text)


def test_delete_student():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails/" + str(IDs[0])
    response = requests.delete(API_URL)
    json_data = response.json()
    msg = jsonpath.jsonpath(json_data, "msg")

    res = requests.get(API_URL)
    json_delete = res.json()
    msg_delete = jsonpath.jsonpath(json_delete, "msg")
    assert msg[0] == 'Delete  data success' and msg_delete[0] == 'No data Found'
