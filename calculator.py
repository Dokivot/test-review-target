import os

DB_PASSWORD = os.environ.get("DB_PASSWORD")

if not DB_PASSWORD:
    raise ValueError("DB_PASSWORD environment variable is not set")


def add(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b


def get_user_data(username):
    # Using parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE name = %s"
    params = (username,)
    return query, params


def process_items(items):
    if items is None:
        return []
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
    try:
        with open("output.txt", "w") as f:
            f.write(result)
    except IOError as e:
        print(f"Error writing to output.txt: {e}")
        return None
    return result


def greet(name):
    return f"Hello {name}"