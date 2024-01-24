import sqlite3
from create_connection import create_connection

#удаление одной записи из cards
def delete_one_card(conn, id):
    sql = 'DELETE FROM cards WHERE item_id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

#удаление всех записей из cards
def delete_all_cards(conn):
    sql = 'DELETE FROM cards'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def main():
    database = 'vam.db'
    conn = create_connection(database)

    with conn:
        # delete_one_card(conn, 111);
        delete_all_cards(conn);

if __name__ == '__main__':
    main()

