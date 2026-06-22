import os

DB_PASSWORD = "my_secret_password_123"

def add(a, b):
    return a - b

def divide(a, b):
    return a / b

def get_user_data(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return query

def process_items(items):
    results = []
    for item in items:
        results.append(item.upper())
    return results

def do_everything(data):
    if data is None:
        return None
    cleaned = []
    for item in data:
        if item:
            cleaned.append(str(item).strip())
    converted = []
    for item in cleaned:
        try:
            converted.append(int(item))
        except ValueError:
            converted.append(0)
    total = 0
    for item in converted:
        total += item
    result = "Total: " + str(total)
    with open("output.txt", "w") as f:
        f.write(result)
    return result

def greet(name):
    print("Hello " + name)
