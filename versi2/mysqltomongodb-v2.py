import mysql.connector
from pymongo import MongoClient
import datetime
import psutil
import time

# conf db mysql 
USER = '' # mysql database username
PASSWORD = '' # mysql database password
HOST = '' # mysql database IP server (localhost or 127.0.01 for local)
DATABASE = 'indomaret'

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
            if type(data_field) is datetime.date:
                t = t + (data_field.strftime("%Y-%m-%d"),)
            else:
                t = t + (data_field,)
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
    for i, k in enumerate(table):
        document = {}
        for j,l in enumerate(columns):
            document[l] = table[i][j]
        result.append(document)
    return result

def insert_into_mongodb(mysql_table, mysql_database, mongodb_collection, mongodb_database):
    collection = get_dict_from_table(mysql_table, mysql_database)
    db = CONNECTION[mongodb_database]
    coll = db[mongodb_collection]
    coll.insert_many(collection)
    
def migrate(database_name):
    cursor.execute('USE {};'.format(database_name))
    cursor.execute('SHOW TABLES;')
    r = cursor.fetchall()
    # print(r)
    print("")
    print("Migrating database {} from MySQL to Mongodb".format(database_name))
    print("")
    i=1
    for item in r:
        print("Migrate table {}: {}".format(i, item[0]))
        start_time = time.time()
        insert_into_mongodb(item[0], database_name, item[0], database_name)
        print('Process {}: Done in {} seconds'.format(i, (time.time() - start_time)))
        i+=1

if __name__ == "__main__":
    r = migrate(DATABASE)