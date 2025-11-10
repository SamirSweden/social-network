import sqlite3


def execute_sql_file(filename,connection):
    with open(filename, 'r', encoding='utf-8') as file:
        sql_script = file.read()
    cursor = connection.cursor()
    try:
        cursor.executescript(sql_script)
        connection.commit()
        print(f"✅ {filename} successfully executed")
    except Exception as e:
        print(f"❌  An error occured {filename}: {e}")


def main():
    conn = sqlite3.connect('social_network.db')

    execute_sql_file('ddl.sql', conn)
    execute_sql_file('dml.sql', conn)
    execute_sql_file('views.sql', conn)

    print("\n=== QUERY TESTING ===")

    cursor = conn.cursor()

    cursor.execute("SELECT id, username, email FROM users")
    users = cursor.fetchall()
    print("👥 Users :")
    for user in users:
        print(f"   {user[0]}: {user[1]} ({user[2]})")

    cursor.execute("SELECT author_username, content FROM post_details LIMIT 3")
    posts = cursor.fetchall()
    print("\n📝 Last posts:")
    for post in posts:
        print(f"   {post[0]}: {post[1][:50]}...")

    conn.close()

if __name__ == "__main__":
    main()
