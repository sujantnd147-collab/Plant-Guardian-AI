"""Small SQLite store for plant profiles and care reminders."""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("plant_guardian.db")

def connect():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    with connect() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS plants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL, species TEXT, planted_on TEXT, notes TEXT
        )""")
        con.execute("""CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plant_name TEXT NOT NULL, task TEXT NOT NULL, due_date TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )""")

def add_plant(name, species="", planted_on="", notes=""):
    with connect() as con:
        con.execute("INSERT INTO plants(name,species,planted_on,notes) VALUES(?,?,?,?)",
                    (name, species, planted_on, notes))

def get_plants():
    with connect() as con:
        return con.execute("SELECT id,name,species,planted_on,notes FROM plants ORDER BY id DESC").fetchall()

def add_reminder(plant_name, task, due_date):
    with connect() as con:
        con.execute("INSERT INTO reminders(plant_name,task,due_date) VALUES(?,?,?)",
                    (plant_name, task, due_date))

def get_reminders():
    with connect() as con:
        return con.execute("SELECT id,plant_name,task,due_date,completed FROM reminders ORDER BY due_date").fetchall()

def complete_reminder(reminder_id):
    with connect() as con:
        con.execute("UPDATE reminders SET completed=1 WHERE id=?", (reminder_id,))
