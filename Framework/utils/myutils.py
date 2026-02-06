import json
import requests

# get all booking
def getAllBooking(url):
    response = requests.get(url)
    data = response.json()
    assert len(data) > 0 and response.status_code == 200
    timetaken = response.elapsed.total_seconds()
    return data, timetaken

def updateBooking(url, booking_id, update_data):
    print("Reqbody: ", json.dumps(update_data))
    response = requests.put(f"{url}/{booking_id}", json=update_data)
    data = response.json()
    return data, response.status_code





