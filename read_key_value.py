import json
with open('key_value_db.json') as file:
    db = json.load(file)

print("key-Value Database:")
for key, value in db.items():
    print(f"{key}: {value}")