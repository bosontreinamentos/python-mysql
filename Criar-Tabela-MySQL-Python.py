import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',
                                         database='db_MeusLivros',
                                         user='root',
                                         password='abc123**')

    criar_tabela_SQL = """CREATE TABLE tbl_produtos ( 
                             IdProduto int(11) NOT NULL,
                             NomeProduto VARCHAR(70) NOT NULL,
                             Preco FLOAT NOT NULL,
                             Quantidade TINYINT NOT NULL,
                             PRIMARY KEY (IdProduto)) """

    cursor = con.cursor()
    result = cursor.execute(criar_tabela_SQL)
    print("Tabela de Produtos criada com sucesso!")

except mysql.connector.Error as error:
    print("Falha ao criar tabela no MySQL: {}".format(error))
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("Conexão ao MySQL finalizada")
