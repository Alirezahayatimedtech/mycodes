import mysql.connector

# برقراری اتصال به دیتابیس
mydb = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database_name"
)

# ایجاد شیء cursor
mycursor = mydb.cursor()

# خواندن اطلاعات از جدول و مرتب کردن بر اساس قد و وزن
mycursor.execute("SELECT Name, Height, Weight FROM employees ORDER BY Height DESC, Weight ASC")

# چاپ نام، قد و وزن هر کارمند به ترتیب مرتب شده
for x in mycursor:
  print(x[0], x[1], x[2])
