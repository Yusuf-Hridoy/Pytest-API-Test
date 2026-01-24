import requests

# First, get an authentication token
auth_url = "https://restful-booker.herokuapp.com/auth"
auth_data = {
    "username": "admin",
    "password": "password123"
}
auth_response = requests.post(auth_url, json=auth_data)
token = auth_response.json()["token"]

# Now delete the booking with authentication
url = "https://restful-booker.herokuapp.com/booking/45"
headers = {
    "Cookie": f"token={token}"
}
response = requests.delete(url, headers=headers)

print(response.status_code)  # Should be 201 for successful deletion
print(response.content)