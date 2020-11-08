print()
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234")
print(mydb)
print("------------------------------------")
print("Insert Multiple Rows in Table:")
print("------------------------------------")
mycursor = mydb.cursor()
mycursor.execute("USE test")
mycursor.execute("CREATE TABLE Students (name VARCHAR(255), address VARCHAR(255))")
sql = "INSERT INTO Students (name, address) VALUES (%s, %s)"
val = [
    ('Rahul', 'Vjayanth Apartments '),
    ('Ayesha', 'Zodiac Apartments '),
    ('Harish', 'Sector 30'),
    ('Sahil', 'Sector 45'),
    ('Yatharth', 'Paramount Apartments'),
    ('Shwetha', 'Sector 20'),
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
