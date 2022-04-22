from mysql.connector import MySQLConnection, Error
from config import config

def item_search(keyword):
    try:
        db_config = config()
        conn = MySQLConnection(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Item WHERE keyword1 = %s or keyword2 = %s or keyword3 = %s", (keyword, keyword, keyword))
        rows = cursor.fetchall()
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)
    except Error as error:
        print(error)
    finally:
        cursor.close()
        conn.close()
        
if __name__ == '__main__':
    item_search('T-Shirt')