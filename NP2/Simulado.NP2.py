"""from random import randint

v1 = []

c1 = 0

c2 = 0

c3 = 0

c4 = 0

c5 = 0

c6 = 0

for i in range(50):
    v1.append(randint(1,6))

print(v1)

for i in range(50):
    if v1[i] == 1:
        c1 = c1 + 1

    elif v1[i] == 2:
        c2 = c2 + 1

    elif v1[i] == 3:
        c3 = c3 + 1

    elif v1[i] == 4:
        c4 = c4 + 1

    elif v1[i] == 5:
        c5 = c5 + 1

    else:
        c6 = c6 + 1

print(f'A ocorrencia de 1 é {((c1/50)*100):.3}%')

print(f'A ocorrencia de 2 é {((c2/50)*100):.3}%')

print(f'A ocorrencia de 3 é {((c3/50)*100):.3}%')

print(f'A ocorrencia de 4 é {((c4/50)*100):.3}%')

print(f'A ocorrencia de 5 é {((c5/50)*100):.3}%')

print(f'A ocorrencia de 6 é {((c6/50)*100):.3}%')"""

########################################################################################################################

"""from random import randint

def rand_key(p):

    key1 = ""

    for i in range(p):

        temp = str(randint(0,1))

        key1 += temp

    return key1

n = randint(1,10)

v1 = []

v2 = []

for i in range(10):

    v1.append(int(rand_key(n)))

for i in range(10):

    str1 = v1[i]

    num = len(str(str1))

    decimal = 0

    i = 0

    while num >=0:

        resto = str1 % 10

        decimal = decimal + (resto*(2**i))

        num = num -1

        i = i +1

        str1 = str1 // 10

    v2.append(decimal)

for i in range(10):
    print(f'O numero binario gerado foi {v1[i]} convertendo para decimal fica: {v2[i]}')"""

########################################################################################################################

"""v1 = []

for i in range(5):
    v1.append(int(input("Digite um numero: ")))

def sub(v2):

    for i in range(5):

        if v2[i] >= 0:
            v2[i] = 1

        else:
            v2[i] = 0

print(v2)

sub(v1)"""

########################################################################################################################

"""import mysql.connector

import datetime

connection = mysql.connector.connect(

host="localhost",

user="root",

password="123456",

database="UNIP22",

)

cursor = connection.cursor()

sql1 = "INSERT INTO Simulado22 (RA, Nome, Nota1, Nota2) VALUES (10, 'Decio', 7.5, 5.5)"

sql2 = "INSERT INTO Simulado22 (RA, Nome, Nota1, Nota2) VALUES (15, 'Decio G', 8.5, 6.5)"

sql3 = "INSERT INTO Simulado22 (RA, Nome, Nota1, Nota2) VALUES (16, 'Decio D', 7.5, 9.5)"

cursor.execute(sql1)

cursor.execute(sql2)

cursor.execute(sql3)

connection.commit()

cursor.close()

connection.close()

print("Os alunos foram cadastrados com sucesso")"""

########################################################################################################################

"""import mysql.connector

import datetime

connection = mysql.connector.connect(

host="localhost",

user="root",

password="123456",

database="UNIP22",

)

cursor = connection.cursor()

comando = f'SELECT * FROM Matricula'

cursor.execute(comando)

resultado = cursor.fetchall()

for i in resultado:
    if (i[2] + i[3])/2 >= 7:
        print("Aluno Aprovado")

    else:
        print("Aluno Reprovado")"""