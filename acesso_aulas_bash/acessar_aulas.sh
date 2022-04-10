#!/bin/bash

dia_semana=$(date +%u)

link=$(echo select link from aulas where diaSemana=$dia_semana | sqlite3 aulas.db) 

if [[ $link =~ [1-5] ]]
then
    firefox $link
else
    echo não há aulas para esse dia 
fi