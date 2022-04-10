#!/usr/bin/python3
import sqlite3 as sq
from datetime import datetime as dt

class aula:
    def __init__(self,diaSemana, nomeAula, horario, link) -> None:
        self.diaSemana = diaSemana
        self.nomeAula = nomeAula
        self.horario = horario
        self.link = link
    def seleciona_horario_da_aula(self):
        horario_atual = dt.now()  # define o dia e a hora atual
        data = horario_atual.strftime('%d/%m/%Y ') # seleciona somente a data para manipular o horario
        
        """ converte de string para datetime para realizar operadores lógigos"""
        data_aula = data + self.horario
        data_aula = dt.strptime(data_aula, '%d/%m/%Y %H:%M')
        data_troca_aula = data + '20:30'
        data_troca_aula = dt.strptime(data_troca_aula, '%d/%m/%Y %H:%M')
        if data_aula < data_troca_aula and horario_atual < data_troca_aula:
            return self.link
        elif data_aula > data_troca_aula and horario_atual > data_troca_aula:
            return self.link
        else:
            return None
if __name__ == '__main__':
    """ define o dia da semana """
    dia_semana = dt.now().weekday() 
    
    """ seleciona o linha da tabela de cordo com o dia da semana """
    banco = sq.connect('/home/barbieri/appaula_db/aulas.db')
    cursor = banco.cursor()
    sql = f'SELECT * FROM links WHERE dia_semana= {dia_semana} '
    cursor.execute(sql)
    links = cursor.fetchall()
    
    """ confere o numero de aulas do dia e chama a classe aula """
    for link in links:
        link_aula = aula(link[0], link[1], link[2], link[3])
        x = link_aula.seleciona_horario_da_aula()
        if x != None:
            print(x)
