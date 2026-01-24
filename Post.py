import requests

url = "https://restful-booker.herokuapp.com/booking" # Endpoint for creating a new booking

booking_data = {
    "firstname" : "yusufxx",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2024-08-23",
        "checkout" : "2024-08-27"
    },
    "additionalneeds" : "Breakfast"
}
response = requests.post(url, json=booking_data)
print(response.status_code) # to see if the request was successful
print(response.content) # to see the raw content of the response

# verify the response is 201
assert response.status_code == 200
