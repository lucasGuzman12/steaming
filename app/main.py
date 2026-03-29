from fastapi import FastAPI
import mysql.connector
import os

app = FastAPI()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

@app.get("/")
def read_root():
    return {"mensaje": "API funcionando"}

@app.get("/usuarios")
def obtener_usuarios():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT 1")
    resultado = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"resultado": resultado}
