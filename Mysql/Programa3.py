import mysql.connector
import datetime

connection = mysql.connector.connect(

    host='localhost',
    user='root',
    password='123456',
    database='Aula15',

)

cursor = connection.cursor()

# UPDATE​

nota = 5
freq = 75

comando = f'UPDATE Matricula SET Nota = "{nota}" WHERE Nota < 5'
comando1 = f'UPDATE Matricula SET Freq = "{freq}" WHERE Freq < 75'

cursor.execute(comando)
cursor.execute(comando1)
connection.commit()