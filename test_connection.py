from database.db import create_connection

conn = create_connection()

if conn.is_connected():
    print("Database Connected Successfully")
else:
    print("Connection Failed")