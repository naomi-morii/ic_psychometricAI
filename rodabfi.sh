#!/bin/bash

# Número de vezes que o programa será executado
n=10  # Defina o valor de n aqui
ini=1
# Caminho para o programa Python
python_script="testeInContext.py"  # Substitua pelo nome do seu script Python

# Loop para rodar o programa n vezes
for ((i=ini; i<n+ini; i++))
do
    # Rodando o programa Python e redirecionando a saída para o arquivo arquivosaida{i}.csv
    python3 $python_script "bfi_responses_incontext$i.csv"
    
    # Opcional: Exibir mensagem indicando que a iteração foi concluída
    echo "Executado $((i-ini+1)) vez(es)"
done

