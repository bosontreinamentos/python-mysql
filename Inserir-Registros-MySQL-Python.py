import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',
                                         database='db_MeusLivros',
                                         user='root',
                                         password='abc123**')

    inserir_dados_autores = """INSERT INTO tbl_autores (NomeAutor, SobrenomeAutor) 
                             VALUES
                             ('Carl','Sagan'),
                             ('Bruce','Schneier'),
                             ('Nivaldo','Tro')"""

    cursor = con.cursor()
    cursor.execute(inserir_dados_autores)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela!")
    cursor.close()

except mysql.connector.Error as error:
    print("Falha ao criar tabela no MySQL: {}".format(error))
finally:
    if (con.is_connected()):
        con.close()
        print("Conexão ao MySQL finalizada")
