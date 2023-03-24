#  pip install mysql-connector-python
# pip install -U autopep8
import mysql.connector as mysql

connection = mysql.connect(
    host="127.0.0.1",
    user="root",
    password="mysql",
    database="ditado"
)
