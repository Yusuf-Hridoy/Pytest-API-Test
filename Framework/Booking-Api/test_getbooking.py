import json
import requests

base_url = "https://restful-booker.herokuapp.com/booking"  # Base endpoint for bookings

def test_get_booking():

    response = requests.get(base_url)
    print(response.status_code)  # to see if the request was successful
    print(response.content)  # to see the raw content of the response

    # validate status code
    assert response.status_code == 200
    # print the response in a pretty format
    
    print(json.dumps(response.json(), indent=4))

    # fetch response header 
    print(response.headers)

def test_get_booking_by_id():
    # Create a booking first to get a valid ID
    booking_data = {
        "firstname": "test_get",
        "lastname": "id_check",
        "totalprice": 123,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-03-01",
            "checkout": "2024-03-05"
        },
        "additionalneeds": "Lunch"
    }
    create_response = requests.post(base_url, json=booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json().get("bookingid")
    print(f"Created booking with ID: {booking_id}")

    # Now verify we can fetch it
    response = requests.get(f"{base_url}/{booking_id}")
    print(response.status_code)  # to see if the request was successful
    print(response.content)  # to see the raw content of the response

    # validate status code
    assert response.status_code == 200
    # print the response in a pretty format
    
    print(json.dumps(response.json(), indent=4))

    # fetch response header 
    print(response.headers)

def test_create_booking():
    booking_data = {
        "firstname": "yusufxx",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-08-23",
            "checkout": "2024-08-27"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(base_url, json=booking_data)
    print(response.status_code)  # to see if the request was successful
    print(response.content)  # to see the raw content of the response

    # verify the response is 201
    assert response.status_code == 200
    # print the response in a pretty format
    
    print(json.dumps(response.json(), indent=4))

    # fetch response header 
    print(response.headers)

   