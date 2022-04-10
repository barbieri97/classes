import sqlite3 as sq

#esse código será executado uma unica vez para criar o banco de dados, após isso ele não tera mais utilidade

""" criando o banco de dados chamado 'aulas.db' """

banco = sq.connect('aulas.db')
cursor = banco.cursor()

""" criando uma lista com os dados que serão inseridos no banco de dados
esses dados estão no arquivo /home/barbieri/linkAulas/link_aulas.txt """

with open( '/home/barbieri/linkAulas/link_aulas.txt', 'r') as arq:
    linhas = arq.readlines()
    lista_aulas = []
    for linha in linhas:
        linha = linha.rstrip()
        lista_aulas.append(linha)
    lista_no_formato_para_db = list()
    for i in lista_aulas:
        i = i.split(',')
        tupla =(i[0], i[1], i[2], i[3])
        lista_no_formato_para_db.append(tupla)

""" criando a tabela 'links' """   

cursor.execute("CREATE TABLE links (dia_semana integer, aula text, horario text, link text)")

cursor.executemany("INSERT INTO links VALUES(?,?,?,?)", lista_no_formato_para_db)
banco.commit()