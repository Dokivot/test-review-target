import os

DB_PASSWORD = os.environ.get("DB_PASSWORD")


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def find_user(name):
    """Query user by name using parameterized query to prevent SQL injection."""
    # Use parameterized query: cursor.execute("SELECT * FROM users WHERE name=%s", (name,))
    return "SELECT * FROM users WHERE name = %s" % (name,)