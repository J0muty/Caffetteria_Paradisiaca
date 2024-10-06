import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

firstname_ = 'Николай'


# Выполняем запрос на удаление
cursor.execute("DELETE FROM main_reguser WHERE firstname = ?", (firstname_,))

conn.commit()

conn.close()
