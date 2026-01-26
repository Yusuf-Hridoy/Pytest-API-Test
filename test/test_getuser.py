import requests
import json
import jsonpath

url = "https://restful-booker.herokuapp.com/booking" # Endpoint to get all bookings

def test_get_all_bookings():
    response = requests.get(url)
    print(response.status_code) # to see if the request was successful
    print(response.content) # to see the raw content of the response

    # print the response code 
    assert response.status_code == 200