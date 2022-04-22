from mysql.connector import MySQLConnection, Error
from config import config

def detail_canceling(detail_id):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("UPDATE Detail SET status = 'canceled' WHERE detail_id = %s", (detail_id,))
        conn.commit()
        print('Successfully canceled detail')
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def order_canceling(order_id):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("UPDATE Order1 SET status = 'canceled' WHERE order_id = %s", (order_id,))
        cursor.execute("UPDATE Detail SET status = 'canceled' WHERE order_id = %s", (order_id,))
        conn.commit()
        print('Successfully canceled order and details')
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    detail_id = '90000001'
    order_id = '901-9717621-9732781'
    
    # detail_canceling(detail_id)
    order_canceling(order_id)