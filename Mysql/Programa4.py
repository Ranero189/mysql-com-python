import mysql.connector
import datetime

connection = mysql.connector.connect(

    host='localhost',
    user='root',
    password="123456",
    database='Aula15'

)

cursor =  connection.cursor()

# DELETE​

comando = f'DELETE FROM Matricula WHERE RA % 2 = 0'

cursor.execute(comando)

connection.commit()  # edita o banco de dados