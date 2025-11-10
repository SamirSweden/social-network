import sqlite3

conn = sqlite3.connect('social_network.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(f"- {table[0]}")

if tables:
    table_name = tables[0][0]
    print(f"\nData from  {table_name}:")
    cursor.execute(f"SELECT * FROM {table_name} LIMIT 5;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in database:")
for table in tables:
    print(f"- {table[0]}")

cursor.execute("SELECT username FROM users WHERE username = 'Over'")
userOver = cursor.fetchall()

print(f"\nUsernames:")

if userOver:
    print(userOver)
else:
    print(f"username in '{tables[0]}' not found")


print("\nAll users (ordered by id):")
cursor.execute("SELECT id, username, email, is_active, created_at FROM users ORDER BY id;")
users = cursor.fetchall()

for user in users:
    print(user)

print("\nAll users (ordered by username):")
cursor.execute("SELECT id, username, email, is_active, created_at FROM users ORDER BY username;")
users = cursor.fetchall()

for user in users:
    print(user)


conn.close()
