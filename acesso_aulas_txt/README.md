# AUTOMAÇÃO ACESSO AS AULAS

Diferente do meu outro repositório acessar_aulas_sqlite, nesse repositório eu trabalho com arquivos de texto para acessar o link das aulas
não é o modo mais eficiente, mas criar esse programa me ajudou a estudar a trabalhar com arquivos de texto com o python

O appaula.sh é um script que abre o navegador e usa o output do script em python
'aula.py' para fornecer o link.

O script aula.py abre um arquivo .txt que contem, entre outras coisas, o link de
acesso, o dia da semana e o horário das aulas, e se baseando no dia da semana, acessa
o link do dia. Caso haja mais de uma aula no dia, o programa confere o horário atual
e entrega o link correspondente a hora.

Existem dois arquivos de texto, um 'link_aulas.txt' e outro 'link_aulas_app.txt'
o primeiro acessa as trasmissões pelo browser e a segunda abre, através do browser,
o aplicativo do zoom.
