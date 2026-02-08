from Framework.utils.myConfigparser import getconfig
from Framework.utils.myutils import getAllBooking, updateBooking, login, deleteBooking

#base_url = "https://restful-booker.herokuapp.com/booking"


base_url = getconfig()

def test_get_all_booking():
    data, timetaken = getAllBooking(base_url)
    print(f"Time taken for the request: {timetaken} seconds")
    print(data)

# update booking by id but need to login first to get the token and then pass the token in the header to update the booking use myutils.login function to get the token and then pass the token in the header to update the booking
def test_update_booking():
    # Create a booking first to get a valid ID
    booking_data = {
        "firstname": "test_update",
        "lastname": "id_check",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-10"
        },
        "additionalneeds": "Breakfast"
    }
    create_response = requests.post(base_url, json=booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json().get("bookingid")
    print(f"Created booking with ID: {booking_id}")

    # login to get the token
    token, status_code = login(base_url.replace("/booking", "/auth"), "admin", "password123")
    assert status_code == 200
    print("Token: ", token)
    
    # update booking by id
    update_data = {
        "firstname": "John_Updated",
        "lastname": "Doe_Updated",
        "totalprice": 200,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-10"
        },
        "additionalneeds": "Dinner"
    }
    data, status_code = updateBooking(base_url, booking_id, update_data, token)
    assert status_code == 200
    print(data)

def test_delete_booking():
    # Create a booking first to get a valid ID
    booking_data = {
        "firstname": "test_delete",
        "lastname": "id_check",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-10"
        },
        "additionalneeds": "Lunch"
    }
    create_response = requests.post(base_url, json=booking_data)
    assert create_response.status_code == 200
    booking_id = create_response.json().get("bookingid")
    print(f"Created booking with ID: {booking_id}")

    # login to get the token
    token, status_code = login(base_url.replace("/booking", "/auth"), "admin", "password123")
    assert status_code == 200
    print("Token: ", token)

    # delete booking by id
    data, status_code = deleteBooking(base_url, booking_id, token)
    assert status_code == 201, f"Expected 201, but got {status_code}"
    print(data)
