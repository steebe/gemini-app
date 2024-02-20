import os
import sqlite3

DB_LOCATION = "./db/app.db"

connection = None
cursor = None

def bootstrap():
  requires_init = not os.path.exists(DB_LOCATION)
  connection = sqlite3.connect(DB_LOCATION)
  cursor = connection.cursor()
  if requires_init:
    cursor.execute("CREATE TABLE history(prompt text, response text)")

def insert_history(prompt, response):
  cursor.execute("INSERT INTO history (prompt, history) VALUES (" + prompt + "," + response + ");")

bootstrap()