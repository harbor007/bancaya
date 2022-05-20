"""
3.- Create a ETL Script pipeline (you can use any language or technology where you are comfortable) to extract evey day at 12 am tehe information of both origins and upload them in to any DWH.
You can add data cleansing process for the data.

"""

# CRONTAB, JUST ADD TO CRON ON A LINUX VIRTUAL MACHINE

# 0 0 * * * /home/jobs/etl.py

from datetime import datetime
from re import A, S
from unittest import result
from defusedxml import ExternalReferenceForbidden
import mysql.connector
import pandas as pd

LM_WRITE_USER = 'user'
LM_WRITE_PASSWORD = 'pass'
LM_WRITE_HOST = 'df_test.com'
LM_WRITE_DATABASE = 'bancaya'
LM_WRITE_PORT = 3306

CONNECTION_STRING = 'mongo_db_cloud_etc'
MONGO_DB = 'test'


def _cnxn(name, mongo_db=None):
    if name == 'mysql':
        cnx = mysql.connector.connect(user = LM_WRITE_USER,
                                    password=LM_WRITE_PASSWORD,
                                    host=LM_WRITE_HOST,
                                    database=LM_WRITE_DATABASE,
                                    port=LM_WRITE_PORT)
        return cnx

    if name == 'nosql':
        client = MongoClient()
        db = client.MONGODB_NAME

        return db[mongo_db]
    
    return print('Connection not defined!')

def extract(query, source, connection):
    if source == 'mysql':
        results = pd.DataFrame(query, connection)
        return results
    if source == 'nosql':
        results == connection.find()
        return results

def transform(results, source):
    if source == 'mysql':
        sales = results.shape[0]
        return sales
    if source == 'nosql':
        sales = len(results)
        return sales

def load(sales, connection):
    try:
        today = datetime.now()
        query_add_cols_map = ("INSERT INTO daily_sales "
                    "(date, sales) "
                    " VALUES (%s, %s)")
        sales_tuple = (today, sales)
        my_cursor = connection.cursor()
        my_cursor.execute(query_add_cols_map, sales_tuple)
        return print('Data loaded')
    except:
        print('Problem loading data.')
        

def main():
    query_select = "SELECT * FROM sales"
    cnx = _cnxn('mysql')
    extract = extract(query_select,'mysql',cnx)
    transform = transform(extract, 'mysql')
    load(transform, cnx)
    cnx.commit()


if __name__ == "__main__":
    # main()
    exit()