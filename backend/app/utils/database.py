import mysql.connector
from mysql.connector import Error

# ✅ Function to connect to MySQL database
def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",  # Change to your MySQL username
            password="root@123",  # Change to your MySQL password
            database="gymDB"
        )
        return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# ✅ Function to create necessary tables
def create_tables():
    conn = get_db_connection()
    if conn is None:
        print("Failed to connect to database.")
        return

    cursor = conn.cursor()
    # Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully!")
