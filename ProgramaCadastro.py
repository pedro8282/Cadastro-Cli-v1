import sqlite3
from sqlite3.dbapi2 import Cursor, Error
from PyQt5 import QtCore, uic, QtWidgets ## Solicita a abertura do QT designer


numer_cod = 0 ### Global


def Banco_dados_clientes():
    
     
        
    nome_cliente = tela2.lineEdit_2.text()
    telefone = tela2.lineEdit_3.text()
    Cpf = tela2.lineEdit_6.text()
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

    limprar_apos_preencher ()

def Banco_dados_produtos():

    produtos = tela2.lineEdit_10.text()
    quantidade = tela2.lineEdit_7.text()
    valor = tela2.lineEdit_8.text()
    
    
    try:
         
            conexao_produtos= sqlite3.connect('Banco_produtos.db')
            cursor = conexao_produtos.cursor(); print("Conectando Banco de dados...")
    
            cursor.execute (""" 
                    CREATE TABLE IF NOT EXISTS Produtoss (
                    cod INTEGER PRIMARY KEY,
                    produtos CHAR(40) NOT NULL,
                    quantidade INTEGER(20),
                    valor INTEGER(11)
                            
                );
            """)
            cursor.execute(""" INSERT INTO Produtoss(produtos, quantidade, valor)
             VALUES(?, ?, ?)""", (produtos , quantidade, valor, ))

            conexao_produtos.commit(); print("Banco de dados Criado.")
            cursor.close()
            conexao_produtos.close()

    except sqlite3.Error as erro:
            print("Erro ao inserir os dados", erro)
            ### Função de click e butão
            
def Listar_produtos():
    
    conexao_produtos= sqlite3.connect('Banco_produtos.db')
    cursor = conexao_produtos.cursor(); print("Conectando Banco de dados...")
    cursor.execute("SELECT * FROM Produtoss") 
    dados_lidoss = cursor.fetchall()
    tela2.tableWidget_2.setRowCount(len(dados_lidoss))
    tela2.tableWidget_2.setColumnCount(4)

    for i in range(0, len(dados_lidoss)):
            
        for k in range(0,4):
                
            tela2.tableWidget_2.setItem(i,k,QtWidgets.QTableWidgetItem(str(dados_lidoss[i][k])))
        
            conexao_produtos.close()   
    
def Listar_dados():
            
    tela3.show() ### Chama a tela 3
    conexao = sqlite3.connect('Banco_cliente.db') ### Chama o banco de dados
    cursor = conexao.cursor() ### Chama o banco de dados
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

def Excluir_produtos():
    linha1 = tela2.tableWidget_2.currentRow()
    tela2.tableWidget_2.removeRow(linha1) 
    conexao_produtos= sqlite3.connect('Banco_produtos.db')
    cursor = conexao_produtos.cursor()

    cursor.execute("SELECT cod FROM Produtoss")
    dados_lidos = cursor.fetchall()
    valor_cod = dados_lidos[linha1][0]
    cursor.execute("DELETE FROM Produtoss WHERE cod="+ str(valor_cod))
    conexao_produtos.commit()

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
    limprar_apos_preencher()
    nome = tela4.lineEdit_8.text()
    login = tela4.lineEdit_5.text()
    senha = tela4.lineEdit_6.text()
    c_senha = tela4.lineEdit_7.text()

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text,login text,senha text)")
            cursor.execute("INSERT INTO cadastro VALUES ('"+nome+"','"+login+"','"+senha+"')")

            banco.commit() 
            banco.close()
            tela4.label_5.setText("Usuario cadastrado com sucesso")

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
        tela4.label_5.setText("As senhas digitadas estão diferentes")
    
def Validar_login():
    limprar_apos_preencher ()
    tela1.label.setText("")
    nome_usuario = tela1.lineEdit.text()
    senha = tela1.lineEdit_2.text()
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()
    try:

        cursor.execute("SELECT senha FROM cadastro  WHERE login ='{}'".format(nome_usuario))
        senha_bd = cursor.fetchall()
        print(senha_bd[0][0])
        banco.close()
        banco.commit()
        
    except :
           
        print("Erro ao inserir os dados", )
         
             
    if  senha == senha_bd[0][0]:  ### Campor editavel 
        tela1.close()
        tela2.show()

    else:
        tela1.label.setText("Senha incorreta")
    limprar_apos_preencher ()
    Listar_produtos()
              
def Cadastrar_user_voltar_tela_login(): ### Sai da tela de cadastro de usuario e volta para o login 
        
    tela4.close()
    tela1.show()

def sai_da_tela_cadastro_clientes(): ### Sai da tela de caadastro de clientes e volta para login
    tela2.close() 
    tela1.show()
    
def sai_tela_login_Abre_Tela_Cadastro_user(): ### sai da tela de login e abre a tela de cadastro de usuarios 
    limprar_apos_preencher ()
    tela1.close()
    tela4.show()
    
def Fecha_login_Programa():### Encerra o programa. 
    tela1.close()

def Altera_dados_volta_tela_De_listaCli():
    tela5.close()
   
def chamar_tela3():
    tela3.show()

def leftMenu():

    
         
     

        ##############################################################################################
        #Páginas do Sistema
        tela2.btn_home.clicked.connect(lambda: tela2.stackedWidget.setCurrentWidget(tela2.pg_home_2))
        tela2.btn_menu_cadastrar.clicked.connect(lambda: tela2.stackedWidget.setCurrentWidget(tela2.page_CADASTRA_3))
        tela2.btn_menu_sobre.clicked.connect(lambda: tela2.stackedWidget.setCurrentWidget(tela2.page_SOBRE_2))
        tela2.btn_menu_contatos.clicked.connect(lambda:tela2.stackedWidget.setCurrentWidget(tela2.pageCONTAATO_2))
        tela2.pushButton_2.clicked.connect(lambda:tela2.stackedWidget.setCurrentWidget(tela2.pageProdutos))
        ###############################################################################################


        width = tela2.left_Menu.width()

        if width == 9:

            newWidth = 200
        else:
            newWidth = 9

        tela2.animation = QtCore.QPropertyAnimation(tela2.left_Menu, b"maximumWidth")
        tela2.animation.setDuration(450)
        tela2.animation.setStartValue(width)
        tela2.animation.setEndValue(newWidth)
        tela2.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        tela2.animation.start()

def seta_D():
    width = tela2.left_Menu.width()

    if width == 9:

        newWidth = 200
    else:
        newWidth = 9

        tela2.animation = QtCore.QPropertyAnimation(tela2.left_Menu, b"maximumWidth")
        tela2.animation.setDuration(450)
        tela2.animation.setStartValue(width)
        tela2.animation.setEndValue(newWidth)
        tela2.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        tela2.animation.start()

def limprar_apos_preencher (): ### Limpa os dados da tela de cadastro 

    ############################### Tela4
    nome = ""
    usuario = ""
    senha_login = ""
    confimacao_senha = ""

    ###############################
    user = ""
    senha = ""
    ############################### Tela1
    Cod = ""
    nome_cliente = ""
    telefone = ""
    Cpf = ""
    Email = ""
    Cidade= ""
    ###############################
    tela4.lineEdit_8.setText(nome)
    tela4.lineEdit_5.setText(usuario)
    tela4.lineEdit_6.setText(senha_login)
    tela4.lineEdit_7.setText(confimacao_senha)
    ###############################
    tela1.lineEdit.setText(user)
    tela1.lineEdit_2.setText(senha)
    ###############################
    tela2.lineEdit.setText(Cod)
    tela2.lineEdit_2.setText(nome_cliente)
    tela2.lineEdit_3.setText(telefone)
    tela2.lineEdit_6.setText(Cpf)
    tela2.lineEdit_4.setText(Email)
    tela2.lineEdit_9.setText(Cidade)

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

tela2.bt_buscar_2.clicked.connect(Listar_dados) 
tela2.pushButton_3.clicked.connect(Listar_produtos)
tela2.bt_sair_2.clicked.connect(sai_da_tela_cadastro_clientes) 
tela2.bt_novo_2.clicked.connect(Banco_dados_clientes)
tela2.pushButton_3.clicked.connect(Banco_dados_produtos)
tela2.btn_toggle.clicked.connect(leftMenu)
tela2.pushButton.clicked.connect(seta_D)  
tela2.bt_buscar_3.clicked.connect(limprar_apos_preencher)  
tela2.pushButton_5.clicked.connect(Excluir_produtos)

tela3.bt_alterar.clicked.connect(Editar_dados)
tela3.bt_apagar.clicked.connect(Excluir_dados)  

tela4.bt_sairtela03_3.clicked.connect(Cadastrar_user_voltar_tela_login)
tela4.pushButton_6.clicked.connect(cadastra_user)

tela5.bt_salvar.clicked.connect(salvar_dados_editados)


 


tela1.show()
app.exec()