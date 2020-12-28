import mysql.connector
from pymongo import MongoClient
import datetime
import psutil

# conf db mysql 
USER = '' # mysql database username
PASSWORD = '' # mysql database password
HOST = '' # mysql database IP server (localhost or 127.0.01 for local)
DATABASE = 'indomaret'
# table to migrate
TABLE_NAME = 'data_barang'

# mysql connection
cnx = mysql.connector.connect(host = HOST, password = PASSWORD, user= USER)
cursor = cnx.cursor()

# mongo connection
CONNECTION = MongoClient('mongodb://localhost')

def get_data_from_table(table, database = DATABASE):
    cursor.execute('USE {};'.format(database))
    cursor.execute('SELECT * FROM {};'.format(table))
    r = cursor.fetchall()
    hasil = []
    # date handler
    for row in r:
        t = ()
        for data_field in row:
            # print(data_field)
            # checking the data type, if date or time convert to string
            if type(data_field) is datetime.date:
                # print(type(data_field))
                # print(data_field)
                t = t + (data_field.strftime("%Y-%m-%d"),)
            else:
                t = t + (data_field,)
        # break
        hasil.append(t)
    return hasil

def get_columns_from_table(table, database = DATABASE):
    cursor.execute('USE {};'.format(database))
    cursor.execute('SHOW COLUMNS FROM {};'.format(table))
    return [item[0] for item in cursor.fetchall()]

def get_dict_from_table(table, database = DATABASE):
    columns = get_columns_from_table(table, database)
    table = get_data_from_table(table, database)
    result = []
    # print(list(enumerate(columns)))
    for i, k in enumerate(table):
        document = {}
        # print(k)
        for j,l in enumerate(columns):
            # print(table[i][j])
            document[l] = table[i][j]
            # print(document[l])
        result.append(document)
    # print(result)
    return result

def insert_into_mongodb(mysql_table, mysql_database, mongodb_collection, mongodb_database):
    collection = get_dict_from_table(mysql_table, mysql_database)
    db = CONNECTION[mongodb_database]
    coll = db[mongodb_collection]
    coll.insert_many(collection)
    
def migrate(database_name, table_name):
    cursor.execute('USE {};'.format(database_name))
    print("Processing Migration")
    print("Migrate table: ", table_name)
    insert_into_mongodb(table_name, database_name, table_name, database_name)
    print('Done')

if __name__ == "__main__":
    r = migrate(DATABASE, TABLE_NAME)