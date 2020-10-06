import requests
import json
import time

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/'





def get_resources(id = None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    resp = requests.get(BASE_URL+END_POINT, data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

get_resources(1)


# def create_resource():
#     new_data = {
#     	'data': 'Test data'
#     }

#     r = requests.post(BASE_URL + END_POINT, data=json.dumps(new_data))
#     print(r.status_code)
#     print(r.json())
# create_resource()






