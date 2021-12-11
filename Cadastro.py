
import sqlite3
from sqlite3.dbapi2 import Cursor
from tkinter.constants import END
from PyQt5 import uic, QtWidgets ### Solicita a abertura do QT designer 

###Criando Banco de Dados 

def salvar_dados():

    nome_cliente = tela.lineEdit_2.text()
    telefone = tela.lineEdit_3.text()
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
                Email CHAR(40),
                Cidade CHAR(40)
                            
             );
        """)
        cursor.execute(""" INSERT INTO clientes(nome_cliente, telefone, Email, Cidade)
         VALUES(?, ?, ?, ?)""", (nome_cliente, telefone , Email, Cidade))

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
    tela_2.tableWidget.setColumnCount(5)

    for i in range(0, len(dados_lidos)):
        for k in range(0,5):
           tela_2.tableWidget.setItem(i,k,QtWidgets.QTableWidgetItem(str(dados_lidos[i][k])))
    
    
    conexao.close()


         


### Chama a aplicação de QTDesigner  

app=QtWidgets.QApplication([])
tela=uic.loadUi("Tela.ui") ### Chama a tela da aplicação feita no QTDsigner
tela_2=uic.loadUi("tela_2.ui")
tela.bt_novo.clicked.connect(salvar_dados)
tela.bt_buscar.clicked.connect(listar_dados)

tela.show()
app.exec()
