## Dir e help + DocStrings de uma linha (Documentação)

Quando possuímos um módulo e queremos saber o que ele possui internamente sem haver a necessidade de abri-lo, podemos utilizar a função especial *"dir"* que retorna uma lista com tudo que há no módulo. ===(Se você não escreveu nada, terá apenas os recursos referentes ao Python nativo)===

Podemos usar qualquer um dos recursos disponibilizados na lista, veja exemplo baixo

```Python
print(uma_linha.__name__) 
# printa o nome do arquivo
print(uma_linha.__file__)
# printa o caminho absoluto do arquivo
```

Além do comando dir, temos o comando *"help"* que da um resumo detalhado do que há no módulo Python em análise. Essa função mostra o nome do arquivo, as funções presentes e os dados, ou variáveis que estão nele, como também o caminho absoluto.

```txt
Help on module uma_linha:

NAME
    uma_linha

FUNCTIONS
    funcao()

DATA
    variavel = 'valor'

FILE
    caminho_absoluto\uma_linha.py
```

A docstring de uma linha pode ser inserida no inicio do módulo para explicar resumidamente o que aquele módulo possibilita fazer e sua aplicabilidade.

Veja um exemplo abaixo no módulo "uma_linha".

```Python
"""O que seu modulo faz"""  
  
variavel = 'valor'  
  
def funcao():  
    return 1
```

