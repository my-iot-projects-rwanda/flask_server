import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO transactions (amount, destination) VALUES (?, ?)",
            (270, 'Gikondo')
            )

cur.execute("INSERT INTO transactions (amount, destination) VALUES (?, ?)",
            (450, 'Kimironko')
            )

connection.commit()
connection.close()
