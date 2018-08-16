#SIMULANDO A ENTRADA DO USUÁRIO

import mysql.connector
import time
mydb = mysql.connector.connect(
  host="192.168.0.7",
  user="rafael",
  passwd="@Renato321",
  database="eventos",
  auth_plugin="mysql_native_password"
)
#auth_plugin="mysql_native_password"
def dataHora():
    t = time.localtime()
    return (str(t.tm_year) + '-' + str(t.tm_mon) + '-' + str(t.tm_mday) + ' ' + str(t.tm_hour) + ':' + str(t.tm_min) + ':' + str(t.tm_sec))

##def sendDB(id_u, temp):    
##    mycursor = mydb.cursor()
##    
##    #Pesquisa o id do usuario
##    mycursor.execute("SELECT ID_CONVIDADO FROM CONVIDADOS WHERE RFID = '{ID}'".format(ID=id_u))
##    id_usuario = mycursor.fetchall()    
##    mycursor.execute("INSERT INTO CCONTROLE VALUES(NULL', {ID_USR}, '{data_hora}');".format(ID_USR = id_usuario[0][0], data_hora = temp)
##    resp = mycursor.fetchall()            
##    #print(resp)
                     
mycursor = mydb.cursor()
mycursor.execute("show databases")
id_usuario = mycursor.fetchall()
print(id_usuario)
uid = 'B7509BAB'
tempo = dataHora()
print(tempo)
mydb.close()
