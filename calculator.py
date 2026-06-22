import os

DB_PASSWORD = os.environ.get("DB_PASSWORD")


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def divide(a, b):
    """Divide a by b, with zero-division check."""
    if b == 0:
        raise ValueError("除数不能为 0")
    return a / b


def get_user_data(username):
    """Query user data using parameterized query to prevent SQL injection."""
    # Use parameterized query: cursor.execute("SELECT * FROM users WHERE name = %s", (username,))
    return "SELECT * FROM users WHERE name = %s" % (username,)


def process_items(items):
    """Convert items to uppercase."""
    results = []
    for item in items:
        results.append(item.upper())
    return results


def do_everything(data):
    """Process data through multiple stages: clean, convert, sum, and save."""
    if data is None:
        return None
    
    # Stage 1: Clean input data
    cleaned = _clean_data(data)
    
    # Stage 2: Convert to integers
    converted = _convert_to_integers(cleaned)
    
    # Stage 3: Calculate total
    total = _calculate_sum(converted)
    
    # Stage 4: Format and save result
    result = "Total: " + str(total)
    _save_result(result)
    
    return result


def _clean_data(data):
    """Remove empty items and strip whitespace."""
    cleaned = []
    for item in data:
        if item:
            cleaned.append(str(item).strip())
    return cleaned


def _convert_to_integers(items):
    """Convert items to integers, defaulting to 0 on failure."""
    converted = []
    for item in items:
        try:
            converted.append(int(item))
        except ValueError:
            converted.append(0)
    return converted


def _calculate_sum(numbers):
    """Calculate sum of numbers."""
    total = 0
    for item in numbers:
        total += item
    return total


def _save_result(result):
    """Save result to output file."""
    with open("output.txt", "w") as f:
        f.write(result)


def greet(name):
    """Print a greeting message."""
    print("Hello " + name)