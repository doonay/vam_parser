import sqlite3
from create_connection import create_connection

def create_table(connection, create_table_sql):
    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def main():
    database = 'vam.db'
    # get connection
    connection = create_connection(database)

    # set tables
    sql_create_cards_table = """CREATE TABLE IF NOT EXISTS cards (
        item_id integer NOT NULL UNIQUE,
        author_name text NOT NULL,
        detail_url text NOT NULL,
        img_local_path text NOT NULL,
        package_name text NOT NULL,
        package_url text NOT NULL,
        blacklist integer DEFAULT 0 NOT NULL CHECK(blacklist >=0 AND blacklist <= 1)
    );"""
    # create tables
    if connection is not None:
        # create cards table
        create_table(connection, sql_create_cards_table)
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()

