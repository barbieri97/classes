# ASSESSANDO AS AULAS REMOTAS

Todos os dias na hora das aulas era uma briga pra achar o link da aula certo

Foi por causa dessa dificuldade que criei esse programa

Ele usa o python `(aula.py)`para fazer consultas no banco de dados e pegar o link da aula do dia e do horário certo

Depois o script em Bash `appaula.sh` para abrir o navegador e acessar o link da aula automaticamente

Ainda usei o python para criar o Banco de dados, esse arquivo é `criando_db.py`, o qual é usado uma unica vez, depois não tem mais utilidade

Os dados são lidos de um arquivo csv tratados e incluidos no banco de dados

O banco de dados utilizado foi o `sqlite`

O arquivo `aulas.db` é o banco de dados que python faz consultas, esse arquivo vai estar vazio por motivos óbvios 
