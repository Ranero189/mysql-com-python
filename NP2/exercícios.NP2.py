"""import mysql.connector

connection = mysql.connector.connect(

    host='localhost',
    user='root',
    password='123456',
    database='CC_UNIP',

)

cursor = connection.cursor()

sql = 'INSERT INTO genios (RA, Nome, Idade, Sexo) VALUES (10, "Decio", 75, "M")'
sql2 = 'INSERT INTO genios (RA, Nome, Idade, Sexo) VALUES (50, "Marco", 20, "F")'
sql3 = 'INSERT INTO genios (RA, Nome, Idade, Sexo) VALUES (40, "Pedro", 19, "M")'
sql4 = 'INSERT INTO genios (RA, Nome, Idade, Sexo) VALUES (30, "Manta", 18, "F")'
sql5 = 'INSERT INTO genios (RA, Nome, Idade, Sexo) VALUES (20, "Ranero", 15, "M")'

cursor.execute(sql)
cursor.execute(sql2)
cursor.execute(sql3)
cursor.execute(sql4)
cursor.execute(sql5)
connection.commit()

print("Os Alunos foram cadastrados com sucesso")

comando = f'SELECT * FROM genios'

cursor.execute(comando)

result = cursor.fetchall()

for row in result:
    print(row)

print('')

M = 0
F = 0
maior_idade = 0

for i in result:
    if i[3] == 'M':
        M += 1
    else:
        F += 1

print(f'Tem {M} meninos e {F} meninas')

for i in result:
    if i[2] > maior_idade:
        maior_idade = i[2]

print('')

for i in result:
    if i[2] >= maior_idade:
        print(f'O Aluno mais velho é {i[1]}')"""

"""from random import randint

mat = [[0 for i in range(3)] for j in range(3)]
mat2 = [[0 for i in range(3)] for j in range(3)]
mat3 = [[0 for i in range(3)] for j in range(3)]

for i in range(3):
    for j in range(3):
        mat[i][j] = randint(1,100)
        mat2[i][j] = randint(1,100)

for i in range(3):
    for j in range(3):
        mat3[i][j] = mat[i][j] + mat2[i][j]

for i in mat:
    print(i)
print('')
for i in mat2:
    print(i)
print('')
for i in mat3:
    print(i)
print('')

for i in range(3):
    for j in range(3):
        print(mat3[i][j], end='  ')
    print('\n')
"""