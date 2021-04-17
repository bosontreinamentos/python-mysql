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
        sql = "SELECT NomeLivro, ISBN13 FROM tbl_livros WHERE IdLivro = 104"
        c.execute(sql)
        res = c.fetchone() # Método fetchone(): retorna uma linha da tabela
        print(res)
        # Acessar o dado retornado pelo nome da coluna
        print('\nLivro retornado:', res['NomeLivro'])
        print()
        # Outra consulta (ainda usando o mesmo cursor): Retornar todas as linhas da tabela de editoras
        sql = "SELECT NomeEditora FROM tbl_editoras"
        c.execute(sql)
        res = c.fetchall() # Método fetchall(): retorna todas as linhas obtidas pela consulta na tabela
        print(res)
        print()
        # Mostrar os dados retornados, um por linha, iterando sobre o resultado:
        for linha in res:
            print(linha['NomeEditora'])
    # Desconectar do servidor
    con.close()

    
    app = QApplication([])
    app.setStyle('Fusion')
    janela = QWidget()
    janela.setWindowTitle('Teste de Qt para Bóson')
    #janela.setGeometry(300,100,350,150)
    janela.resize(400,400)
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    #layout.addWidget(QLabel('Bóson Treinamentos!'))

    label = QLabel('Bóson Treinamentos!')
    layout.addWidget(label)

    # Botão que abre caixa de alerta:
    botao = QPushButton('Clique Aqui')
    layout.addWidget(botao)
    botao.clicked.connect(clicar_botao)
    botao.show()

    # ComboBox:
    frutas = ['Abacate','Morango','Melancia','Kiwi','Maçã','Caju']
    cmbFrutas = QComboBox()
    cmbFrutas.addItems(frutas)
    layout.addWidget(cmbFrutas)

    janela.setLayout(layout)
    janela.show()

    app.exec_()
