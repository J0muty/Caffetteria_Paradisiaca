import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

email_ = 'tix1@mail.ru'

cursor.execute("DELETE FROM main_reguser WHERE email = ?", (email_,))

conn.commit()
conn.close()
