import sqlite3
def create_db():
    con=sqlite3.connect(database=r'db.sqlite3')
    cur=con.cursor("CREATE TABLE IF NOT EXISTS sub")