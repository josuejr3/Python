# Exercicio
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos
# a data em que ela pegou o empréstimo foi 20/12/2020
# e o vencimento de cada parcela é no dia 20 de cada mês
# - crie a data de emprestimo
# - crie a data final do emprestimo
# - mostre todas as datas de vencimento e o valor de cada parcela
from calendar import month
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_emprestimo = datetime.strptime("20/12/2022", "%d/%m/%Y")

# python permite separar numeros grandes com _
# ex: 1_000_000

valor_parcela = 1_000_000 / 60
soma = 0

for i in range(5):
    for j in range(12):
        print(datetime.strftime(data_emprestimo, "%d/%m/%Y"), f"Parcela {j+1}: R$ {valor_parcela:,.2f}")
        data_emprestimo = data_emprestimo + relativedelta(months=+1)
        soma += 16666.67




