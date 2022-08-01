import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Dss89.sql',
    database='banco',
)

cursor = conexao.cursor()


#CRUD V2 (in progress)

#CREATE
nome = "Dionata"
telefone = 5199887766
email = "dionata@email.com"
comando = f'INSERT INTO cadastroclientes (nome, telefone, email) VALUES ("{nome}", {telefone}, "{email}")'
cursor.execute(comando)
conexao.commit()

#READ
rd = f'SELECT * FROM cadastroclientes'
cursor.execute(rd)
resultado = cursor.fetchall()
print(resultado)

#UPDATE
nome = "Dionata"
email = "dionata@email.com"
telefone = 1198889888
att = f'UPDATE cadastroclientes SET telefone = {telefone} WHERE nome = "{nome}"'
cursor.execute(att)
conexao.commit()

#DELETE
nome = "Dionata"
apagar = f'DELETE FROM cadastroclientes WHERE nome = "{nome}"'
cursor.execute(apagar)
conexao.commit()

cursor.close()
conexao.close()
