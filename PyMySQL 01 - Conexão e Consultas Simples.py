import pymysql

# Não esquecer de instalar o pacote "cryptography" antes.
# Abrir uma conexão a um banco de dados
con = pymysql.connect(host='localhost', user='root', database='db_MeusLivros',cursorclass=pymysql.cursors.DictCursor,password='abc123**')


if __name__ == '__main__':
    # Preparar um cursor com o método .cursor()
    with con.cursor() as c:
        # Criar uma consulta e executá-la no banco :Retornar todas as linhas da tabela de editoras
        sql = "SELECT nomeEditora FROM tbl_editoras"
        c.execute(sql)
        res = c.fetchall()
        print(res)
        print()
        for linha in res:
            print(linha['nomeEditora'])

        # Outra consulta, com cláusula WHERE
        sql2 = "SELECT nomeLivro, isbn13 FROM tbl_livros WHERE idLivro = 4"
        c.execute(sql2)
        res2 = c.fetchone()
        print(res2)
        # Acessar dado pelo nome da coluna
        print('\nLivro retornado:', res2['nomeLivro'])
        print('ISBN do livro:', res2['isbn13'])
        print()

    # Desconectar do servidor
    con.close()
