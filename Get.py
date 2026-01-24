
import requests

url = "https://restful-booker.herokuapp.com/booking"

response = requests.get(url)
print(response.status_code) # to see if the request was successful
print(response.content) # to see the raw content of the response

# validate status code
assert response.status_code == 200
# print the response in a pretty format
print(response.json())

# fetch response header 
print(response.headers)

# parse json response
json_response = response.json()
print(json_response)

# want booking id value 0-5
for i in range(50):
    print(json_response[i]['bookingid'])