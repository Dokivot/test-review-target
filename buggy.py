DB_PASSWORD = "hardcoded_secret_123"          # 硬编码密钥

def add(a, b):
    return a - b                                # 逻辑错误

def find_user(name):
    return "SELECT * FROM users WHERE name='" + name + "'"  # SQL 注入
