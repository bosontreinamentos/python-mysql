import mysql.connector
from mysql.connector import Error
# Inserir registros em um banco de dados MySQL

try:
    con = mysql.connector.connect(host='localhost',database='db_MeusLivros',user='root',password='abc123**')

    inserir_produtos = """INSERT INTO tbl_produtos
                            (IdProduto, NomeProduto, Preco, Quantidade) 
                          VALUES
                            (1,'Câmera',850.00,5),
                            (2,'Monitor',630.00,7),
                            (3,'Relógio',575.00,10)
                       """
    cursor = con.cursor()
    cursor.execute(inserir_produtos)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela!")
    cursor.close()
except Error as erro:
    print("Falha ao inserir dados no MySQL: {}".format(erro))
finally:
    if (con.is_connected()):
        con.close()
        print("Conexão ao MySQL finalizada")
