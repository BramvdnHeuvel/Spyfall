import sqlite3

def init_database():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("DROP TABLE IF EXISTS 'counter'")
    c.execute("CREATE TABLE 'counter' ('number' INTEGER NOT NULL DEFAULT 0)")
    c.execute("INSERT INTO 'counter' VALUES (0)")

    conn.commit()
    conn.close()

def get_counter():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("UPDATE 'counter' SET number = number + 1")
    conn.commit()

    c.execute("SELECT * FROM 'counter'")
    return c.fetchone()[0]

if __name__ == "__main__":
    init_database()
    print(get_counter())
    print(get_counter())
    print(get_counter())