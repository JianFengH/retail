from mysql.connector import MySQLConnection, Error
from config import config
from datetime import datetime

def order_insert(order_id, customer_id, status):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Order1 (order_id, customer_id, status, date) VALUES (%s, %s, %s, %s)", (order_id, customer_id, status, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
        print('Total Row(s):', cursor.rowcount)
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def detail_insert(detail_id, order_id, item_id, item_count, status):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Detail (detail_id, order_id, item_id, item_count, status) VALUES (%s, %s, %s, %s, %s)", (detail_id, order_id, item_id, item_count, status))
        conn.commit()
        print('Total Row(s):', cursor.rowcount)
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()

def order_making(order_id, customer_id, detail_id, item_id, item_count):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        status = 'created'
        cursor.execute("INSERT INTO Order1 (order_id, customer_id, status, date) VALUES (%s, %s, %s, %s)", (order_id, customer_id, status, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        cursor.execute("INSERT INTO Detail (detail_id, order_id, item_id, item_count, status) VALUES (%s, %s, %s, %s, %s)", (detail_id, order_id, item_id, item_count, status))
        conn.commit()
        print('Successfully inserted order and detail')
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    order_id = '901-9717621-9732781'
    customer_id = '3465474'
    detail_id = '90000001'
    item_id = '901001-01'
    item_count = 2

    # order_insert(order_id, customer_id, 'created')
    # detail_insert(detail_id, order_id, item_id, item_count, 'created')

    order_making(order_id, customer_id, detail_id, item_id, item_count)