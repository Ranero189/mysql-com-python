import mysql.connector
import datetime

conexao = mysql.connector.connect(

    host='localhost',
    user='root',
    password="123456",
    database='Aula15'

)

cursor = conexao.cursor()

# READ​

comando = f'SELECT * FROM Matricula'

cursor.execute(comando)
resultado = cursor.fetchall()  # ler o banco de dados​

for row in resultado:
    print(row)

print('')

for i in resultado:
    if i[2] >= 5 and i[3] >=75:
        print("Aluno Aprovado")
    else:
        print("Aluno Reprovado")