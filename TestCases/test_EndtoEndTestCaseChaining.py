import json
import requests
import jsonpath
from pprint import pprint as pp
import pytest
from .Library import Common


@pytest.mark.P0
@pytest.mark.Integression
def test_add_new_data():
    global Id
    obj = Common("https://thetestingworldapi.com/api/studentsDetails",
                 "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\RequestJosn.json")
    api_url, json_request = obj.common_steps()
    response = requests.post(api_url, json_request)
    # print(response.text)
    json_data = response.json()
    Id = jsonpath.jsonpath(json_data, "id")
    assert len(Id) != 0, "Insertion failed for new student"
    # print(Id[0])


@pytest.mark.Regression
def test_update_tech_skills():
    obj = Common("https://thetestingworldapi.com/api/technicalskills",
                 "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\TechSkill.json")
    api_url, tech_json_request = obj.common_steps()
    tech_json_request['id'] = int(Id[0])
    tech_json_request['st_id'] = Id[0]

    tech_response = requests.post(api_url, tech_json_request)
    # print(tech_response.text)
    assert (jsonpath.jsonpath(tech_response.json(), 'status')[0] == 'true' and
            jsonpath.jsonpath(tech_response.json(), 'msg')[0] == 'Add  data success')


@pytest.mark.Regression
def test_update_addresses():
    obj = Common("https://thetestingworldapi.com/api/addresses",
                 "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\AddressJson.json")
    api_url, add_json_request = obj.common_steps()
    add_json_request['stId'] = Id[0]

    add_response = requests.post(api_url, add_json_request)
    # print(add_response.text)
    assert (jsonpath.jsonpath(add_response.json(), 'status')[0] == 'true' and
            jsonpath.jsonpath(add_response.json(), 'msg')[0] == 'Add  data success')


@pytest.mark.Validate
def test_get_final_detail_of_new_student():
    final_detail_url = "https://thetestingworldapi.com/api/FinalStudentDetails/" + str(Id[0])
    final_response = requests.get(final_detail_url)
    # pp(final_response.text)
    assert jsonpath.jsonpath(final_response.json(), "data.TechnicalDetails")[0][0]['st_id'] == str(Id[0])
