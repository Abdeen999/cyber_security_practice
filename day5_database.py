import sqlite3

# 1. Connect to database
connection = sqlite3.connect("my_hacking_lab.db")
cursor = connection.cursor()

# 2. Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS targets (
    id INTEGER PRIMARY KEY,
    ip_address TEXT,
    port_number INTEGER,
    status TEXT
)
""")

# 3. Insert data
cursor.execute("INSERT INTO targets (ip_address, port_number, status) VALUES (?, ?, ?)", ("127.0.0.1", 80, "CLOSED"))

# 4. Save changes
connection.commit()

# 5. Fetch and print data
cursor.execute("SELECT * FROM targets")
rows = cursor.fetchall()
print("--- Database Results ---")
for row in rows:
    print(row)

# 5. Close connection
connection.close()