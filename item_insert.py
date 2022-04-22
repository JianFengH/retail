from mysql.connector import MySQLConnection, Error
from config import config

def item_insert(item_id, shop_id, name, price, stock, keyword1, keyword2, keyword3):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Item (item_id, shop_id, name, price, stock, keyword1, keyword2, keyword3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (item_id, shop_id, name, price, stock, keyword1, keyword2, keyword3))
        conn.commit()
        print('Total Row(s):', cursor.rowcount)
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    item_insert('901001-01', '9001009', 'NIKE TShirt', 189, 3000, 'T-Shirt', 'Shirt', 'Fashion')