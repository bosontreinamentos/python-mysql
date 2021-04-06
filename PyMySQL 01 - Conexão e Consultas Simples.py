import pymysql.cursors

con = pymysql.connect(host='localhost',user='root',password='abc123**',database='db_MeusLivros',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

with con.cursor() as c:
    # Ler um registro único
    sql = "SELECT NomeLivro, ISBN13 FROM tbl_livros WHERE IdLivro = 104"
    c.execute(sql)
    res = c.fetchone()
    print(res)


with con.cursor() as c:
    # Retornar todas as linhas da tabela de editoras
    sql = "SELECT NomeEditora FROM tbl_editoras"
    c.execute(sql)
    res = c.fetchall()
    print(res)

    for linha in res:
        print(linha['NomeEditora'])

con.close
