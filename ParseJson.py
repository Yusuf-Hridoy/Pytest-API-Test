import json

# dictionary
data = {
    "name": "John Doe", 
    "age": 30, 
    "city": "New York",
}

json_result = json.dumps(data)

print(json_result)