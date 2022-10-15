import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

data = cursor.execute("SELECT name, halal FROM food").fetchall()
print(data)
