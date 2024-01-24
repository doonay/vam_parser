import sqlite3
from create_connection import create_connection

#выборка всех записей из cards
def select_all_cards(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM cards")

    rows = cur.fetchall()

    for row in rows:
        print(row)

#выборка записей из cards по автору
def select_task_by_author(conn, author_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM cards WHERE author_name=?", (author_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

def main():
    database = 'vam.db'

    # create a database connection
    conn = create_connection(database)

    with conn:
        print("1. Query task by author:")
        select_task_by_author(conn, 'GoodAuthor')

        print("2. Query all tasks:")
        select_all_cards(conn)

if __name__ == '__main__':
    main()
'''
если разбивать таблицу, то запрос на селект потом джойнить
Select * from card t1 join author t2 on t1.fk_id = t2.id where t2.author_name = …
'''
