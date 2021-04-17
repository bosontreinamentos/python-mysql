from PyQt5.QtWidgets import *
import pymysql


def conectaBanco():
    global con
    con = pymysql.connect(host='localhost',user='root',database='db_MeusLivros',cursorclass=pymysql.cursors.DictCursor,password='abc123**')
    
def clicar_botao():
    alert = QMessageBox()
    alert.setText('Bóson Treinamentos!')
    alert.exec()

def msg_problema_BD():
    msg_problema = QMessageBox()
    msg_problema.setText('Problema ao obter os dados. Tente novamente.')
    msg_problema.exec()

if __name__=="__main__":

    # Preparar um cursor com o método .cursor()
    conectaBanco()
    with con.cursor() as c:
        # Criar a consulta e executá-la no banco
        sql = "SELECT NomeEditora FROM tbl_editoras"
        c.execute(sql)
        res = c.fetchall()
        # Criar lista com os dados retornados
        listaEditoras = []
        for linha in res:
            listaEditoras.append(linha['NomeEditora'])
    # Desconectar do servidor
    con.close()

    app = QApplication([])
    app.setStyle('Fusion')
    janela = QWidget()
    janela.setWindowTitle('Teste de Qt para Bóson')
    #janela.setGeometry(300,100,350,150)
    janela.resize(400,400)
    layout = QVBoxLayout()

    # Botão que abre caixa de alerta:
    botao = QPushButton('Clique Aqui')
    layout.addWidget(botao)
    botao.clicked.connect(clicar_botao)
    botao.show()

    label = QLabel('Lista de Editoras:')
    layout.addWidget(label)
    
    # ComboBox do banco de dados:
    cmbEditoras = QComboBox()
    cmbEditoras.addItems(listaEditoras)
    layout.addWidget(cmbEditoras)

    # Pesquisa de Livros por ID
    labelLivros = QLabel('Digite o código do livro a pesquisar:')
    txtIdLivro = QLineEdit()
    txtNomeLivro = QLineEdit()
    botaoLivro = QPushButton('Pesquisar Livro')

    def consulta_livro():
        try:
            conectaBanco()
            IdLivro = txtIdLivro.text()
            with con.cursor() as c:
                sql = "SELECT NomeLivro FROM tbl_livros WHERE IdLivro = " + IdLivro + ";"
                c.execute(sql)
                res = c.fetchone()
                txtNomeLivro.setText(res['NomeLivro'])
        except Exception:
            msg_problema_BD()
        finally:
            con.close()

    layout.addWidget(labelLivros)
    layout.addWidget(txtIdLivro)    
    layout.addWidget(botaoLivro)
    layout.addWidget(txtNomeLivro)
    botaoLivro.clicked.connect(consulta_livro)
    botaoLivro.show()
    
    janela.setLayout(layout)
    janela.show()

    app.exec_()
