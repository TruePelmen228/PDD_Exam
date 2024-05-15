import sqlite3 as sl

base = sl.connect('data.db')

with base:
    data = base.execute("select count(*) from sqlite_master where type='table' and name='filler'")
    
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
             base.execute("""

CREATE TABLE IF NOT EXISTS answers (
    session_number INTEGER PRIMARY KEY
                           NOT NULL
                           UNIQUE,
    time_m         INTEGER,
    time_s         INTEGER,
    right_answers  INTEGER
);

            """)

