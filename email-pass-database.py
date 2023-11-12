import re
from mysql import connector


cnx = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)


cursor = cnx.cursor()


query = "INSERT INTO users (email, password) VALUES (%s, %s)"


email = input("Enter email: ")
password = input("Enter password: ")


pattern = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

while not re.match(pattern, email):
    print('Invalid email format. Please enter a valid email address.')
    email = input('Enter email: ')


cursor.execute(query, (email, password))


cnx.commit()


cursor.close()
cnx.close()
