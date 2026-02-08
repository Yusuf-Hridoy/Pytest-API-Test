import json
import requests

# get all booking
def getAllBooking(url):
    response = requests.get(url)
    data = response.json()
    assert len(data) > 0 and response.status_code == 200
    timetaken = response.elapsed.total_seconds()
    return data, timetaken

def updateBooking(url, booking_id, update_data, token):
    print("Reqbody: ", json.dumps(update_data))
    headers = {"Cookie": f"token={token}"}
    response = requests.put(f"{url}/{booking_id}", json=update_data, headers=headers)
    data = response.json()
    return data, response.status_code

# In Framework/utils/myutils.py
def login(url, username, password):
    response = requests.post(url, json={"username": username, "password": password})
    
    if response.status_code != 200:
        raise Exception(f"Login failed with status {response.status_code}: {response.text}")
    
    data = response.json()
    return data.get("token"), response.status_code

# delete booking
def deleteBooking(url, booking_id, token):
    headers = {"Cookie": f"token={token}"}
    response = requests.delete(f"{url}/{booking_id}", headers=headers)
    try:
        data = response.json()
    except json.JSONDecodeError:
        data = "Deleted"
    return data, response.status_code

