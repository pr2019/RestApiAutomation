import requests
import json
import jsonpath
import openpyxl
from DataDrivenTest import Library


def test_add_multiple_students():
    API_URL = "https://thetestingworldapi.com/api/studentsDetails"
    f = "C:\\Users\\prade\\PycharmProjects\\ApiTesting\\TestCases\\RequestJosn.json"
    json_input = open(f, 'r')
    json_request = json.loads(json_input.read())

    obj = Library.Common("C:/Users/prade/PycharmProjects/ApiTesting/TestCases/AddStudentsAData.xlsx", "Sheet1")
    col = obj.fetch_column_count()
    row = obj.fetch_row_count()
    keylist = obj.fetch_key_names()

    for i in range(2, row + 1):
        update_req = obj.update_req_with_data(i, json_request, keylist)
        response = requests.post(API_URL, update_req)
        print(response.text)
