import json
import requests
ids = [
   
]


url = "http://168.119.115.32:8082/api/devices"


def add_device(serial, id):
    payload = json.dumps({
        "name": f"Vehicle {serial}",
        "uniqueId": id,
        "status": "OFF",
        "disabled": False,
        "lastUpdate": "2022-10-14T00:15:22Z",
        "positionId": 0,
        "groupId": 0,
        "phone": "string",
        "model": "string",
        "contact": "string",
        "category": "string",
        "geofenceIds": [
            0
        ],
        "attributes": {}
    })
    headers = {
        'Authorization': 'Basic YWRtaW46YWRtaW4=',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(id, response.status_code)

for i, v in enumerate(ids):
    add_device(i+4, v)