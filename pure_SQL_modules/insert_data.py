import sqlite3
from create_connection import create_connection

#вставка по одному объекту в cards
def insert_one_card(connection, card):
    sql = ''' INSERT OR IGNORE INTO cards(
        item_id,
        author_name,
        detail_url,
        img_local_path,
        package_name,
        package_url,
        blacklist
    )VALUES(?,?,?,?,?,?,?) '''
    cursor = connection.cursor()
    cursor.execute(sql, card)
    connection.commit()
    return cursor.rowcount

#вставка сразу нескольких объектов
def insert_cards(connection, cards):
    sql = ''' INSERT OR IGNORE INTO cards VALUES(?,?,?,?,?,?,?); '''
    cursor = connection.cursor()
    cursor.executemany(sql, cards);
    connection.commit()
    return cursor.rowcount

def main():
    database = 'vam.db'
    connection = create_connection(database)

    with connection:
        card_1 = (123, 'GoodAuthor', 'http://detail_1', '/home/1', 'package_1', 'http://package_1', 0)
        card_2 = (456, 'MiddleAuthor', 'http://detail_2', '/home/2', 'package_2', 'http://package_2', 0)
        card_3 = (555, 'BadAuthor', 'http://detail_2', '/home/2', 'package_2', 'http://package_2', 0)
        result = insert_one_card(connection, card_1)
        print(f'Добавлена {result} запись')
        result = insert_one_card(connection, card_2)
        print(f'Добавлена {result} запись')
        result = insert_one_card(connection, card_3)
        print(f'Добавлена {result} запись')

        cards = [
            (123, 'FuckAuthor', 'http://detail_1', '/home/1', 'package_1', 'http://package_1', 0),
            (111, 'GoodAuthor', 'http://detail_2', '/home/2', 'package_2', 'http://package_2', 0),
            (333, 'GodFather', 'http://detail_2', '/home/2', 'package_2', 'http://package_2', 0)
        ]
        result = insert_cards(connection, cards)
        print(f'Добавлена {result} запись')

if __name__ == '__main__':
    main()

'''
если разбивать таблицу, то запрос на селект потом джойнить
Select * from card t1 join author t2 on t1.fk_id = t2.id where t2.author_name = …
'''