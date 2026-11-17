import sqlite3

# 1. میموری میں ایک عارضی ڈیٹا بیس بناتے ہیں اور 'admin' یوزر سیٹ کرتے ہیں
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)
''')
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret123')")
conn.commit()

print("--- SQL Injection Local Test Lab ---\n")

# 2. ان پٹ لیں
# ہیکر کی طرح ٹیسٹ کرنے کے لیے یوزر نیم میں یہ لکھیں: admin' --
username = input("Enter username: ")
password = input("Enter password: ")

print("\n-----------------------------------------")
print("1. Testing VULNERABLE Code (using f-string):")
print("-----------------------------------------")

# غیر محفوظ طریقہ (f-string کے ذریعے براہ راست ان پٹ ملانا)
vulnerable_query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
print(f"Query sent to DB: {vulnerable_query}")

try:
    cursor.execute(vulnerable_query)
    result = cursor.fetchone()
    if result:
        print(">>> [ALERT] Login Successful! (SQL Injection worked, password bypassed!)")
    else:
        print(">>> Login Failed.")
except Exception as e:
    print(f">>> Error: {e}")


print("\n-----------------------------------------")
print("2. Testing SECURE Code (using Parameters):")
print("-----------------------------------------")

# محفوظ طریقہ (Parameterization استعمال کرتے ہوئے)
secure_query = "SELECT * FROM users WHERE username = ? AND password = ?"
print(f"Query template: {secure_query}")

cursor.execute(secure_query, (username, password))
secure_result = cursor.fetchone()

if secure_result:
    print(">>> Login Successful (Normal valid login).")
else:
    print(">>> [BLOCKED] Login Failed! (SQL Injection successfully neutralized).")
