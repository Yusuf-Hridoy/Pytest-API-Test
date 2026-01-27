import requests

login_url = "https://restful-booker.herokuapp.com/auth" # Endpoint to get auth token
delete_url = "https://restful-booker.herokuapp.com/booking/44" # Endpoint to delete a booking

def test_delete_booking():
    # First, get the authentication token
    auth_data = {
        "username": "admin",
        "password": "password123"
    }

    auth_response = requests.post(login_url, json=auth_data)
    token = auth_response.json().get("token")

    headers = {
        "Cookie": f"token={token}"
    }

    response = requests.delete(delete_url, headers=headers)
    print(response.status_code) # to see if the request was successful
    print(response.content) # to see the raw content of the response

    # print the response code 
    assert response.status_code == 201