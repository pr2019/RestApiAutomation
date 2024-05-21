import json
import requests
import jsonpath
import openpyxl

class Common:
    def __init__(self, URL, FilePath):
        global API_URL
        global FileLocation

        API_URL = URL
        FileLocation = FilePath

    def common_steps(self):
        f = open(FileLocation, 'r')
        json_obj = json.loads(f.read())

        return API_URL, json_obj



