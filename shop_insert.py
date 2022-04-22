from mysql.connector import MySQLConnection, Error
from config import config

def shop_insert(shop_id, name, rating, location):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Shop (shop_id, name, rating, location) VALUES (%s, %s, %s, %s)", (shop_id, name, rating, location))
        conn.commit()
        print('Total Row(s):', cursor.rowcount)
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    shop_insert('9001009', 'NIKE', 100, 'Hong Kong')