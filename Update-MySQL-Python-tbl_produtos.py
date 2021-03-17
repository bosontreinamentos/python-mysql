import mysql.connector
from mysql.connector import Error

# Atualizar registros em um banco de dados MySQL

def conectar():
    try:
        global con
        con = mysql.connector.connect(host='localhost',database='db_MeusLivros',user='root',password='abc123**')
    except Error as erro:
        print("Erro de Conexão")

def atualiza(declaracao):
    try:
        conectar()
        altera_preco = declaracao
        cursor = con.cursor()
        cursor.execute(altera_preco)
        con.commit()
        print("Preço alterado com sucesso!")
        cursor.close()
    except Error as erro:
        print("Falha ao inserir dados no MySQL: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()

def consulta(idProd):
    try:
        conectar()
        consulta_sql = 'select * from tbl_produtos WHERE IdProduto = ' + idProd
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall()

        for linha in linhas:
            print("Id:", linha[0])
            print("Produto:", linha[1])
            print("Preço:", linha[2])
    except Error as erro:
        print("Falha ao consultar tabela: {}".format(erro))
    finally:
        if (con.is_connected()):
            cursor.close()
            con.close()
    

if __name__=='__main__':
    
    print("Rotina para atualização de preços produtos no banco de dados")
    print("Entre com os dados conforme solicitado:")

    print("\nDigite o codigo do produto a alterar:")
    idProd = input("Id do Produto: ")

    consulta(idProd)

    print("\nEntre com o novo preço do produto:")
    precoProd = input("Preço: ")

    declaracao = """UPDATE tbl_produtos
    SET Preco = """ + precoProd + """
    WHERE IdProduto = """ + idProd

    atualiza(declaracao)
    
    verifica = input("\nDeseja consultar a atualização? s = Sim, n = Não\n")
    if (verifica == 's'):
        consulta(idProd)
    else:
        print("\nAté mais!")
