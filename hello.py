from fastapi import FastAPI
import sqlite3

connection = sqlite3.connect("test.db")
cursor = connection.cursor()

app = FastAPI()
value_return = []

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

@app.get("/foods/")
async def get_foods():
    value_return = []
    data = cursor.execute("SELECT name, halal FROM food").fetchall()
    for i in data:
        value_return.append({"Food Name": i[0],"Halal": i[1]})
    return value_return