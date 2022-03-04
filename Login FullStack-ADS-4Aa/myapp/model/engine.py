import json
import pyodbc
def retornar_conexao_sql():
    server = "LAPTOP-7R3VIR6J\ADS_TCC"
    database = "FullStackLogin"
    #username = "aula_mongodb"
    #password = "abc123"
    #string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao
    
#cursor.execute("Insert into [dbo].[User] ([UserLogin],[UserEmail],[UserPassword]) VALUES ('?','?','?')")
#conexao.commit()

def CadastrarUsuario(Unome,Uemail,Upassword):
    sql ="Insert into [dbo].[User] ([UserLogin],[UserEmail],[UserPassword]) VALUES (?,?,?)"
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute(sql, (Unome,Uemail,Upassword))
    cursor.commit()
    cursor.close()
    return (Unome,"Cadastrado")

def VerificarUsuario(Uemail,Upassword):
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    sql ="SELECT UserLogin FROM [dbo].[User] WHERE UserEmail = ? and UserPassword = ?"
    cursor.execute(sql, (Uemail,Upassword))
    nome = cursor.fetchone()
    cursor.commit()
    cursor.close()
    if nome == None:
        return("Digitou algo errado tente novamente")
    return ("AEE PARABENS VOCÊ LOGOU",nome)
def TodosUsuarios():
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM [dbo].[User]")
    Users = cursor.fetchall()
    mylist =[]
    for x in Users:
        mylist.append(x)
    return mylist