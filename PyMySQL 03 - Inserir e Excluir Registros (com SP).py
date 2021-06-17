import pymysql
import getpass

if __name__ == '__main__':

    # Criar objeto para conexão ao banco de dados pedindo senha ao usuário
    #print('Digite a senha para conexão ao banco de dados:')
    senha = getpass.getpass('Digite a senha para conexão ao banco de dados:')
    con = pymysql.connect(host='localhost', user='root', cursorclass=pymysql.cursors.DictCursor,
                          database='db_meuslivros', password=senha)

    with con.cursor() as c:
        # Consulta a ser realizada:
        sql = 'SELECT NomeLivro, ISBN13 FROM tbl_Livros WHERE IDLivro = 4'
        c.execute(sql)
        res = c.fetchone()
        #print(res)
        print('Livro:', res['NomeLivro'])
        print('ISBN:', res['ISBN13'])

    # ----------------------------------------------------------
    # Inserir um registro na tabela de assuntos
    assunto = input('Digite o assunto a cadastrar e pressione enter: ')
    with con.cursor() as cur:
        sql = "INSERT INTO tbl_assuntos (Assunto) VALUES ('" + assunto + "');"
        cur.execute(sql)
        con.commit()
        cur.close()

    with con.cursor() as cur:
        # Retornar todas as linhas da tabela de assuntos
        sql = "SELECT Assunto FROM tbl_assuntos"
        cur.execute(sql)
        res = cur.fetchall()
        for item in res:
            print(item['Assunto'])

    #----------------------------------------------------------
    # Excluir um registro da tabela de assuntos
    
    # 1. Descobrir o ID a excluir:
    print('Digite o assunto a excluir e pressione enter:')
    assunto = input()
    with con.cursor() as cur:
        # Retornar todas as linhas da tabela de assuntos
        sql = "SELECT IdAssunto FROM tbl_assuntos WHERE Assunto = " + "'" + assunto + "';"
        cur.execute(sql)
        res = cur.fetchone()
        print('ID do Assunto: {}'.format(res['IdAssunto']))
    # 2. Executar a rotina de exclusão:
        #sql = "DELETE FROM tbl_assuntos WHERE IdAssunto =  " + "'" + str(res['IdAssunto']) + "';"
        sql = "call sp_del_assunto(" + str(res['IdAssunto']) + ");" # usando stored procedure
        cur.execute(sql)
        con.commit()
    # 3. Verificar a exclusão:
        sql = "SELECT Assunto FROM tbl_assuntos"
        cur.execute(sql)
        res = cur.fetchall()
        for item in res:
            print(item['Assunto'])
        cur.close()
    # ----------------------------------------------------------
    
    # Não esquecer de fechar a conexão!
    con.close()
