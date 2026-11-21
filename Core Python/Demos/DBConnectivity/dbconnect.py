import mysql.connector
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="emp"
)
if con.is_connected:
    print("DB Connected")
cursor=con.cursor()
query="select * from emp"
cursor.execute(query)
record=cursor.fetchall()
print(record)