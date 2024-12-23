# Colete os dígitos do CPF - Somente números e sem caracteres especiais

# Pegar os primeiros nove números e multiplicar por uma contagem regressiva 10-2

# Somar os resultados das multiplicações

# Multiplica o resultado por 10

# Fazer o resto da divisão do número obtido anteriormente, por 11

# Se o resultado da divisão for maior que 9 o resultado do dígito é 0
# Se for diferente o dígito é o resultado

# =============================================================================
# Usando expressões regulares

import re
import sys

while True:

    try:
        cpf = input("Digite o número do CPF: ")

        # Removendo pontos, espaços e ífens ( COM EXPRESSOES REGULARES )
        # Poderia ter usado o replace
        cpf = re.sub('[^0-9]', '', cpf)
        if len(cpf) == 11:
            try:

                # Testando se o número passado é composto apenas de números
                cpf_int = int(cpf)
                primeito_caractere = cpf[0]

                if cpf == primeito_caractere * len(cpf):
                    print("CPF inválido")
                    continue

                # Definindo o primeiro dígito
                nove_digitos = cpf[:9]
                resultado_multiplicacoes_digito_1 = 0
                contador_regressivo_1 = (10, 9, 8, 7, 6, 5, 4, 3, 2)

                for i in range(len(nove_digitos)):
                    resultado_multiplicacoes_digito_1 += int(nove_digitos[i]) * contador_regressivo_1[i]

                digito_1 = ((10 * resultado_multiplicacoes_digito_1) % 11)
                digito_1 = digito_1 if digito_1 <= 9 else 0

                # Definindo o segundo dígito   ( Fazer uma função que recebe iterável )
                dez_digitos = nove_digitos + str(digito_1)
                resultado_multiplicacoes_digito_2 = 0
                contador_regressivo_2 = (11, 10, 9, 8, 7, 6, 5, 4, 3, 2)

                for j in range(len(dez_digitos)):
                    resultado_multiplicacoes_digito_2 += int(dez_digitos[j]) * contador_regressivo_2[j]

                digito_2 = (10 * resultado_multiplicacoes_digito_2) % 11
                digito_2 = digito_2 if digito_2 <= 9 else 0

                cpf_gerado = dez_digitos + str(digito_2)
                print("CPF validado com sucesso" if cpf == cpf_gerado else "CPF invalido")

            # Se o valor não conseguir ser convertido, ele retorna um erro
            except ValueError:
                print("CPF inválido, tente novamente sem caracteres especiais, por favor")

        else:
            print("CPF com caracteres a mais ou a menos, verifique e tente novamente")

    except KeyboardInterrupt:
        print("\nPrograma encerrado")
        break


# Poderia ter usado como um gerador de CPF usando a biblioteca randint para
# gerar os números do CPF.
