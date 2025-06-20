import json

with open('wide_column_db.json') as file:
    db = json.load(file)

print("Wide-Column Database (Users Table):")
for row_key, row_data in db['users'].items():
    print(f"{row_key}: {row_data}")