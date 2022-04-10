#!/usr/bin/python3
from datetime import datetime as dt
import time as t

""" determinando o dia da semana e o horario que o programa esta sendo
executado """
hora_e_data_atual = dt.now()
dia_da_semana = dt.today()
dia_semana = dia_da_semana.weekday()
dia_semana = str(dia_semana)

""" definido o horario das trocas das aulas """
troca_da_aula = dt.now()
troca_da_aula = troca_da_aula.strftime('%d/%m/%Y')
troca_da_aula += ' 20:30'  #selecionar arbitrariamente o horario das 20:30
horario_da_toca = dt.strptime(troca_da_aula, '%d/%m/%Y %H:%M') 
# não encontrei uma forma de trabalhar somente com o horário sem as datas

""" lendo o arquivo de texto com as informações das aulas """
with open('path/to/link_aulas_app.txt', 'r') as file:
    todas_aulas = file.readlines()

    """removendo os \n e colocando as linhas dentro de uma lista"""
    lista = []
    for x in todas_aulas:
        x = x.rstrip()
        lista.append(x)

    """ selecionando as aulas do dia """    
    lista_aula = []
    for x in lista:
        if x[0] == dia_semana:
            lista_aula.append(x)

    """ separando as string das aulas do dia e adicionando a uma lista
    para trabalhar com cada elemento separadamente  """
    aulas_do_dia = []
    for aula in lista_aula:
        q = aula.split(',')     # dia da semena = [0]
        aulas_do_dia.append(q)  # nome da aula = [1]
                                # hora da aula = [2]
                                # link da aula = [3]
    """ verificando se há mais de uma aula no dia e caso haja
    selecionar a aula correspondente ao horario """
    if len(aulas_do_dia) == 1:
        print(aulas_do_dia[0][3])
    else:
        if hora_e_data_atual < horario_da_toca:
            print(aulas_do_dia[0][3])
        else:
            print(aulas_do_dia[1][3])
