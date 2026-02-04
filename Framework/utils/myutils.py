import requests

# get all booking
def getAllBooking(url):
    response = requests.get(url)
    data = response.json()
    assert len(data) > 0 and response.status_code == 200
    return data





