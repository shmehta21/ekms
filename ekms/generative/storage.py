import sqlite3
import os
from datetime import datetime

DB_FILE = "ekms.db"
DOC_DIR = "documents"
os.makedirs(DOC_DIR, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    preset TEXT,
                    input TEXT,
                    output TEXT,
                    timestamp TEXT
                )""")
    conn.commit()
    conn.close()

def save_generated(preset, input_text, output_text):
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO history (preset, input, output, timestamp) VALUES (?, ?, ?, ?)",
              (preset, input_text, output_text, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

def get_history():
    init_db()
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT preset, input, output, timestamp FROM history ORDER BY id DESC LIMIT 10")
    rows = c.fetchall()
    conn.close()
    return [{"preset": r[0], "input": r[1], "output": r[2], "timestamp": r[3]} for r in rows]
