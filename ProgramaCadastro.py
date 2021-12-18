import sqlite3
from PyQt5 import uic, QtWidgets ## Solicita a abertura do QT designer

numer_cod = 0

def Banco_dados_clientes():
        
    nome_cliente = tela2.lineEdit_2.text()
    telefone = tela2.lineEdit_3.text()
    Cpf = tela2.lineEdit_5.text()
    Email = tela2.lineEdit_4.text()
    Cidade= tela2.lineEdit_9.text()
    
    
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
        ### Função de click e butão
        tela2.bt_novo.clicked.connect(Banco_dados_clientes)

def Listar_dados():

        
    tela3.show()
    conexao = sqlite3.connect('Banco_cliente.db')
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    dados_lidos = cursor.fetchall()
    tela3.tableWidget.setRowCount(len(dados_lidos))
    tela3.tableWidget.setColumnCount(6)

    for i in range(0, len(dados_lidos)):
            
        for l in range(0,6):
                
            tela3.tableWidget.setItem(i,l,QtWidgets.QTableWidgetItem(str(dados_lidos[i][l])))
        
            conexao.close()       
     
def Editar_dados():
    global numer_cod
    linha = tela3.tableWidget.currentRow()
    conexao = sqlite3.connect('Banco_cliente.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT cod FROM clientes")
    clientes = cursor.fetchall()
    valor_cod = clientes[linha][0]
    cursor.execute("SELECT * FROM clientes WHERE cod="+ str(valor_cod))
    cliente = cursor.fetchall()
    tela5.show()
    
    numer_cod = valor_cod

    tela5.lineNome.setText(str(cliente[0][1]))
    tela5.lineTelefone.setText(str(cliente[0][2]))
    tela5.linecpf.setText(str(cliente[0][3]))
    tela5.lineEmail.setText(str(cliente[0][4]))
    tela5.lineEndereco.setText(str(cliente[0][5]))

def salvar_dados_editados():
    global numer_cod
    ### valores digitados no lineEdit
    nome_cliente = tela5.lineNome.text()
    telefone = tela5.lineTelefone.text()
    Cpf = tela5.linecpf.text()
    Email = tela5.lineEmail.text()
    Cidade= tela5.lineEndereco.text()
    ### Atualizar os dados do banco
    conexao = sqlite3.connect('Banco_cliente.db')
    cursor = conexao.cursor(); print("Conectando Banco de dados...")
    cursor.execute("UPDATE clientes SET nome_cliente = '{}', telefone = '{}', Cpf = '{}', Email ='{}', Cidade = '{}' WHERE cod = {}".format(nome_cliente,telefone,Cpf,Email,Cidade,numer_cod))
    conexao.commit()
    tela5.close()
    tela3.close()
    Listar_dados()
     
def Excluir_dados():
    linha = tela3.tableWidget.currentRow()
    tela3.tableWidget.removeRow(linha) 
    conexao = sqlite3.connect('Banco_cliente.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT cod FROM clientes")
    dados_lidos = cursor.fetchall()
    valor_cod = dados_lidos[linha][0]
    cursor.execute("DELETE FROM clientes WHERE cod="+ str(valor_cod))
    conexao.commit()
   
def cadastra_user():    

    nome = tela4.lineEdit_8.text()
    nome_user = tela4.lineEdit_5.text()
    senha = tela4.lineEdit_6.text()
    C_senha = tela4.lineEdit_7.text()

    if (senha == C_senha):
            
        try:

            user = sqlite3.connect("Banco_user.db")
            cursor = user.cursor(); print("Conectando Banco de dados...")
    
            cursor.execute (""" 
                        CREATE TABLE IF NOT EXISTS User (
                        nome CHAR(40) NOT NULL,
                        nome_user CHAR(40) NOT NULL,
                        senha INTEGER(20) NOT NULL,
                        C_senha INTEGER(11) NOT NULL
                                            
                    );
                """)
            cursor.execute(""" INSERT INTO User(nome, nome_user, senha, C_senha)
                            VALUES(?, ?, ?, ?)""", (nome,nome_user, senha, C_senha))

            user.commit(); print("Banco de dados Criado.")
            cursor.close()
            tela4.label_5.setText("Usuario Cadastrado com Sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados", erro)

    
    else:
        tela4.label_5.setText("As senha digitadas são divergentes.")
    
def Validar_login():
    tela2.label.setText("")
    usuario = tela1.lineEdit.text()
    senha = tela1.lineEdit_2.text() 
    user = sqlite3.connect("Banco_user.db")
    cursor = user.cursor()
    try:

        cursor.execute("SELECT senha FROM User WHERE nome_user='{}'".format(usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
    except:
        print("Erro ao inserir os dados")
        tela_erro.show()
    
    
    if usuario == "Pedro2021" and senha == "123456" :  ### Campor editavel 
        tela1.close()
        tela2.show()

    else:
        print("Dados incorreto")
              
def Cadastrar_user_voltar_tela_login(): ### Sai da tela de cadastro de usuario e volta para o login 
        
    tela4.close()
    tela1.show()

def sai_da_tela_cadastro_clientes(): ### Sai da tela de caadastro de clientes e volta para login
    tela2.close() 
    tela1.show()
    
def sai_tela_login_Abre_Tela_Cadastro_user(): ### sai da tela de login e abre a tela de cadastro de usuarios 
    tela1.close()
    tela4.show()
    
def Fecha_login_Programa():### Encerra o programa. 
    tela1.close()

def Altera_dados_volta_tela_De_listaCli():
    tela5.close()
   
def chamar_tela3():
    tela3.show()


app=QtWidgets.QApplication([])

tela1=uic.loadUi("tela1.ui")### Chama a tela da aplicação feita no QTDsigner
tela2=uic.loadUi("tela2.ui")### Chama a tela da aplicação feita no QTDsigner
tela3=uic.loadUi("tela3.ui")### Chama a tela da aplicação feita no QTDsigner
tela4=uic.loadUi("tela4.ui")### Chama a tela da aplicação feita no QTDsigner
tela5=uic.loadUi("tela5.ui")### Chama a tela da aplicação feita no QTDsigner
tela_erro=uic.loadUi("tela_erro.ui")### Chama a tela da aplicação feita no QTDsigner
 
tela1.bt_sairtela03.clicked.connect(Fecha_login_Programa)
tela1.pushButton_2.clicked.connect(sai_tela_login_Abre_Tela_Cadastro_user)
tela1.pushButton.clicked.connect(Validar_login)

tela2.bt_buscar.clicked.connect(Listar_dados)
tela2.bt_sair.clicked.connect(sai_da_tela_cadastro_clientes) 
tela2.bt_novo.clicked.connect(Banco_dados_clientes) 

tela3.bt_alterar.clicked.connect(Editar_dados)
tela3.bt_apagar.clicked.connect(Excluir_dados)



tela4.bt_sairtela03_3.clicked.connect(Cadastrar_user_voltar_tela_login)
tela4.pushButton_6.clicked.connect(cadastra_user)

tela5.bt_salvar.clicked.connect(salvar_dados_editados)


 


tela1.show()
app.exec()