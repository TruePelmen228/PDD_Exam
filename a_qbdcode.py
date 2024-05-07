import sqlite3 as sl

base = sl.connect('data.db')

with base:
    data = base.execute("select count(*) from sqlite_master where type='table' and name='filler'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
             base.execute("""
                 CREATE TABLE answers(
                 session_number INTEGER,
                 number INTEGER,
                 time TIME,
                 right_answers INTEGER
                 );
            """)
