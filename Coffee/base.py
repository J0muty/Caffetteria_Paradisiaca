import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

email_to_delete = 'dds-49@yandex.ru'

# Выполняем запрос на удаление
cursor.execute("DELETE FROM main_reguser WHERE email = ?", (email_to_delete,))

conn.commit()

conn.close()
