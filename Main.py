
import pymysql 
print("----------------1------------------")
host = 'localhost'
user = 'root'
password = '12345'
database = 'blogdb'
print("-------------------2-----------------")
# Connect to the database
try:
    #connection = pymysql.connect(**db_config)

    # Establishing the connection 
    connection = pymysql.connect(host=host, user=user, password=password, database=database)
    print("-------------------3-----------------")
    cursor = connection.cursor()
    print("-------------------4-----------------")
    print("Connected to the database successfully.")
except Exception as e:
    print(f"Failed to connect to the database: {e}")
    exit()