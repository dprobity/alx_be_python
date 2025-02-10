import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", passwd= "$$Probity500!@$$", database="abc", port=3306 )

    if mydb.is_connected():
        print("connected successfully")

except mysql.connector.Error as err:
    print(f"Error: {err}")





mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS customer (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(255) NOT  NULL,
email VARCHAR(255) NOT NULL UNIQUE
)
"""
)


mydb.commit()

print("Table created successfully")