
def connect_db():
    import mysql.connector

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mulinhas", #"MUL1NH4S"
        database="testes"
    )
    return mydb

def create_users_table():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "CREATE TABLE users (user varchar(20), senha varchar(20), email varchar(40), admin bool);"
    mycursor.execute(sql)
    mydb.commit()

def create_oss_table():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    sql = "CREATE TABLE oss (Sala varchar(3), Maquina varchar(2), Problema varchar(50), Reportado varchar(100), Resolvido varchar(18));"
    mycursor.execute(sql)
    mydb.commit()
    

def Insert_Login(Usuario, Senha, Email, Técnico):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()


    sql = "INSERT INTO users (user, senha, email, admin) VALUES (%s, %s, %s, %s)"
    val = [user, senha, email, admin]

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def Insert_OS(Sala, Maquina, Problema, Reportado, Resolvido):
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    # CREATE TABLE bd (user varchar(20), senha varchar(20), data varchar(10));
    # CREATE TABLE oss (Sala varchar(3), Maquina varchar(2), Problema varchar(50), Reportado varchar(100), Resolvido varchar(18))

    sql = "INSERT INTO oss (Sala, Maquina, Problema, Reportado, Resolvido) VALUES (%s, %s, %s, %s, %s)"
    val = [Sala, Maquina, Problema, Reportado, Resolvido]

    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")


def Select_Login():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM login")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)


def Select_OS():
    import mysql.connector

    mydb = connect_db()
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM oss")
    myresult = mycursor.fetchall()
    return myresult


'''
Funções Existentes:
    connect_db() # criar conexão com banco de dados
        Insert_Login()
            Insert_OS()
                Select_Login()
                    Select_OS()
'''