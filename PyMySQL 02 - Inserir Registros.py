import pymysql.cursors

con = pymysql.connect(host='localhost',user='root',password='abc123**',database='db_MeusLivros',charset='utf8mb4')
# conexão irá retornar tupla em vez de dicionário neste exemplo.

assunto = input('Digite o assunto a cadastrar e pressione enter: ')

#Inserir um registro na tabela de assuntos
with con.cursor() as cur:
    sql = "INSERT INTO tbl_assuntos (Assunto) VALUES " + "('" + assunto + "');"
    cur.execute(sql)
    con.commit()
    cur.close()

with con.cursor() as cur:
    # Retornar todas as linhas da tabela de assuntos
    sql = "SELECT Assunto FROM tbl_assuntos"
    cur.execute(sql)
    res = cur.fetchall()
    for item in res:
        print(item[0]) # usamos 0 pois atributos de tupla são números, e não índices

con.close
