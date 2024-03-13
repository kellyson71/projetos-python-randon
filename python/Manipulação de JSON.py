import json

# Dicionário para JSON
data = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

json_data = json.dumps(data)
print("JSON:", json_data)

# JSON para Dicionário
decoded_data = json.loads(json_data)
print("Decoded Data:", decoded_data)
