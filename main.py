import psycopg2.pool
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Create a connection pool with a minimum of 2 connections and 
#a maximum of 3 connections 
pool = psycopg2.pool.SimpleConnectionPool( 
    2,
    3, 
    user=os.environ.get('PG_USER'),
    password=os.environ.get('PG_PASSWORD'), 
    host=os.environ.get('PG_HOST'), 
    port='5432', 
    database=os.environ.get('PG_DB'))


connection1 = pool.getconn() 
  
# Use the connection to execute a query 
cursor = connection1.cursor() 
print("Results from Connection1: \n") 
cursor.execute('SELECT * FROM person ORDER BY id') 
results = cursor.fetchall() 
for data in results: 
    print(data) 
    print()

connection2 = pool.getconn() 
# Use the connection to execute a query 
cursor = connection2.cursor() 
print("Results from Connection2: \n") 
cursor.execute('SELECT * FROM person ORDER BY id') 
results = cursor.fetchall() 
for data in results: 
    print(data) 
    print() 
  
connection3 = pool.getconn() 
  
# Use the connection to execute a query 
cursor = connection3.cursor() 
print("Results from Connection3: \n") 
cursor.execute('SELECT * FROM person ORDER BY id') 
results = cursor.fetchall() 
for data in results: 
    print(data) 
    print()

pool.putconn(connection1) 
pool.putconn(connection2) 
pool.putconn(connection3)