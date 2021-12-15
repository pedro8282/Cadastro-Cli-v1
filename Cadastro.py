
import sqlite3
from sqlite3.dbapi2 import Cursor
from tkinter.constants import END
from PyQt5 import uic, QtWidgets ### Solicita a abertura do QT designer 

###Criando Banco de Dados 
def login():
    tela.label.setText("")
    usuario = tela_03.lineEdit.text()
    senha = tela_03.lineEdit_2.text()
    
    if usuario == "Pedro2021" and senha == "123456" :     ### Campor editavel 
        tela_03.close()
        tela.show()

    else:
        tela_03.label.setText("Dados incorretos!")
def sair():
    tela.close() 
    
    tela_03.show()
def sair_login():
    tela_03.close()
def salvar_dados():

    nome_cliente = tela.lineEdit_2.text()
    telefone = tela.lineEdit_3.text()
    Cpf = tela.lineEdit_5.text()
    Email = tela.lineEdit_4.text()
    Cidade= tela.lineEdit_9.text()
    
    
    try:

        conexao = sqlite3.connect('Banco_cliente.db')
        cursor = conexao.cursor(); print("Conectando Banco de dados...")
    
        cursor.execute (""" 
                CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                Cpf INTEGER(11),
                Email CHAR(40),
                Cidade CHAR(50)
                            
             );
        """)
        cursor.execute(""" INSERT INTO clientes(nome_cliente, telefone, Cpf, Email, Cidade)
         VALUES(?, ?, ?, ?, ?)""", (nome_cliente, telefone , Cpf, Email, Cidade, ))

        conexao.commit(); print("Banco de dados Criado.")
        cursor.close()
        conexao.close()

    except sqlite3.Error as erro:
        print("Erro ao inserir os dados", erro)
def listar_dados():
    tela_2.show()
    conexao = sqlite3.connect('Banco_cliente.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    dados_lidos = cursor.fetchall()
    tela_2.tableWidget.setRowCount(len(dados_lidos))
    tela_2.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
        for l in range(0,6):
           tela_2.tableWidget.setItem(i,l,QtWidgets.QTableWidgetItem(str(dados_lidos[i][l])))
    
    
    conexao.close()
    

### Chama a aplicação de QTDesigner  

app=QtWidgets.QApplication([])
tela_03=uic.loadUi("tela_03.ui")### Chama a tela da aplicação feita no QTDsigner
tela=uic.loadUi("Tela.ui") ### Chama a tela da aplicação feita no QTDsigner
tela_2=uic.loadUi("tela_2.ui")### Chama a tela da aplicação feita no QTDsigner
tela_03.pushButton.clicked.connect(login)
tela.bt_novo.clicked.connect(salvar_dados)
tela.bt_buscar.clicked.connect(listar_dados)

tela.bt_sair.clicked.connect(sair)
tela_03.bt_sairtela03.clicked.connect(sair_login)

tela_03.show()

app.exec()
