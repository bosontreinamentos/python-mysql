from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import pymysql
import sys


def conectaBanco():
    global con
    con = pymysql.connect(host='localhost',user='root',database='db_MeusLivros',cursorclass=pymysql.cursors.DictCursor,password='abc123**')
    
def clicar_botao():
    alert = QMessageBox()
    alert.setWindowTitle('Bem-vindos!')
    alert.setText('Bóson Treinamentos!')
    alert.exec()

def msg_problema_BD():
    msg_problema = QMessageBox()
    msg_problema.setWindowTitle('Problema')
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
    
    layout = QGridLayout()

    # Margens esquerda, acima, direita, abaixo:
    layout.setContentsMargins(50,0,20,10)
    # Espaçamento entre elementos:
    layout.setSpacing(10)


    # Botão que abre caixa de alerta:
    botao = QPushButton('Clique Aqui')
    layout.addWidget(botao,0,0)
    botao.clicked.connect(clicar_botao)
    botao.show()

    label = QLabel('Lista de Editoras:')
    layout.addWidget(label,1,0)
    
    # ComboBox do banco de dados:
    cmbEditoras = QComboBox()
    cmbEditoras.addItems(listaEditoras)
    layout.addWidget(cmbEditoras,2,0)

    # Caixa de texto para mostrar item selecionado no ComboBox
    txtEditora = QLineEdit()
    layout.addWidget(txtEditora,3,0)
    def informaEditora():
        txtEditora.setText(cmbEditoras.currentText())
    cmbEditoras.activated.connect(informaEditora)

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

    layout.addWidget(labelLivros,0,1)
    layout.addWidget(txtIdLivro,1,1)    
    layout.addWidget(botaoLivro,2,1)
    layout.addWidget(txtNomeLivro,3,1)
    botaoLivro.clicked.connect(consulta_livro)
    botaoLivro.show()
    
    janela = QWidget()
    janela.setWindowTitle('Teste de Qt para Bóson')
    #janela.setGeometry(300,100,350,150)
    janela.resize(400,200) # largura, altura
    janela.setLayout(layout)
    janela.show()

    sys.exit(app.exec_())

    
