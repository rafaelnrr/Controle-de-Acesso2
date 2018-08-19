# -*- coding: utf-8 -*-

# SIMULANDO A ENTRADA DO USUÁRIO

import mysql.connector
import time

mydb = mysql.connector.connect(
  host="192.168.0.7",
  user="rafael",
  passwd="@Renato321",
  database="eventos",
  auth_plugin="mysql_native_password"
)


def data_hora():
    t = time.localtime()
    hora = str(t.tm_hour)
    minuto = str(t.tm_min)
    segundo = str(t.tm_sec)

    dia = str(t.tm_mday)
    mes = str(t.tm_mon)
    ano = str(t.tm_year)

    if t.tm_hour < 10:
        hora = "0" + str(t.tm_hour)
    if t.tm_min < 10:
        minuto = "0" + str(t.tm_min)
    if t.tm_sec < 10:
        segundo = "0" + str(t.tm_sec)

    if t.tm_mday < 10:
        dia = "0" + str(t.tm_mday)
    if t.tm_mon < 10:
        mes = "0" + str(t.tm_mon)
    if t.tm_year < 10:
        ano = "0" + str(t.tm_year)

    return (ano + '-' + mes + '-' + dia + ' ' + hora + ':' + minuto + ':' + segundo)

def verificar_banco(id_u, temp):

    pesquisa_usuario  = mydb.cursor()

    id_usuario = 1

    try:
        # Pesquisa o id do usuario
        pesquisa_usuario.execute("SELECT ID_CONVIDADO FROM CONVIDADOS WHERE RFID = '{ID}'".format(ID=id_u))
        resposta = pesquisa_usuario.fetchall()
        pesquisa_usuario.close()
        if(resposta):
            for resultado in resposta:
                id_usuario = resultado[0]
        else:
            print("Convidado não encontrado!")
            return

    except mysql.connector.Error as err:
        print(err)
        return

    armazena_controle = mydb.cursor()
    try:
        armazena_controle.execute("""INSERT INTO CONTROLE VALUES(NULL, {ID_USR}, '{data_h}');""".format(ID_USR = id_usuario, data_h = str(temp)))
        mydb.commit()
    except mysql.connector.Error as err:
        if err.errno == 1062:
            print("Atenção! Convidado já entrou.")


    try:
        resposta = armazena_controle.fetchall()
        armazena_controle.close()
    except mysql.connector.Error as err:
        armazena_controle.close()



uid = 'A879BAB'
tempo = data_hora()
verificar_banco(uid, tempo)
mydb.close()
