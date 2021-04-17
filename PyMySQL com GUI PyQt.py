from PyQt5.QtWidgets import *
import pymysql

con = pymysql.connect(host='localhost',user='root',database='db_MeusLivros',cursorclass=pymysql.cursors.DictCursor,password='abc123**')

def clicar_botao():
    alert = QMessageBox()
    alert.setText('Bóson Treinamentos!')
    alert.exec()

if __name__=="__main__":

    # Preparar um cursor com o método .cursor()
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
    layout = QHBoxLayout()

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

    janela.setLayout(layout)
    janela.show()

    app.exec_()
