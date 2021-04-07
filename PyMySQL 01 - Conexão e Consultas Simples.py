import pymysql.cursors

# Abrir uma conexão a um banco de dados
con = pymysql.connect(host='localhost',user='root',database='db_MeusLivros',cursorclass=pymysql.cursors.DictCursor,password='abc123**')

# Preparar um cursor com o método .cursor()
with con.cursor() as c:
    # Criar ma consulta e executá-la no banco
    sql = "SELECT NomeLivro, ISBN13 FROM tbl_livros WHERE IdLivro = 104"
    c.execute(sql)
    res = c.fetchone()
    print(res)
    # Acessar dado pelo nome da coluna
    print('Livro retornado:', res['NomeLivro'])

print()
with con.cursor() as c:
    # Retornar todas as linhas da tabela de editoras
    sql = "SELECT NomeEditora FROM tbl_editoras"
    c.execute(sql)
    res = c.fetchall()
    print(res)
    print()
    for linha in res:
        print(linha['NomeEditora'])

# Desconectar do servidor
con.close()
