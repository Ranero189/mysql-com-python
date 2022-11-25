import mysql.connector
import datetime

connection = mysql.connector.connect(

    host="localhost",
    user="root",
    password="123456",
    database="Aula15"

) 

cursor = connection.cursor()

sql = "INSERT INTO Matricula (RA, Nome, Nota, Freq) VALUES (10, 'Decio Lago', 7.5, 75)"
sql1 = "INSERT INTO Matricula (RA, Nome, Nota, Freq) VALUES (25, 'Fernanda G.', 5.0, 50)"
sql2 = "INSERT INTO Matricula (RA, Nome, Nota, Freq) VALUES (11, 'Decio M.', 3.4, 65)"
sql3 = "INSERT INTO Matricula (RA, Nome, Nota, Freq) VALUES (24, 'Fernanda D.', 4.5, 75)"
sql4 = "INSERT INTO Matricula (RA, Nome, Nota, Freq) VALUES (15, 'Decio r.', 5.5, 75)"


cursor.execute(sql)
cursor.execute(sql1)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
connection.commit()

cursor.close() 
connection.close()

print("Os Alunos foram cadastrados com sucesso")
