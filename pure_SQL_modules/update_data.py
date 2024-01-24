import sqlite3
from create_connection import create_connection

#обновление данных
def update_one_card(conn, card):
    sql = ''' UPDATE cards SET blacklist = ? WHERE item_id = ?'''
    cur = conn.cursor()
    cur.execute(sql, card)
    conn.commit()


def main():
    database = 'vam.db'

    # create a database connection
    conn = create_connection(database)

    with conn:
        update_one_card(conn, (1, 333)) # обновить значение blacklist на 1, где item_id = 333

if __name__ == '__main__':
    main()

