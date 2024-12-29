# Tipo - Dicionários

# Criando o dicionário pessoa

# Usamos a chave como se fosse o índice

# PAR - INDICE:VALOR

# Tipos que podem ser chave/índice em dicionários: mutáveis
# int, float, str, bool, tuple

# Tipos que podem ser valor: tudo

# Dicionarios são mutaveis

people = {
    "name": "Josue",
    "surname": "Ferreira",
    "age": 24,
    "height": 1.72,
    "address": [
        {"rua": "tal tal", "número": 123},
        {"rua": "outra rua", "numero": 321}
    ]
}

# Funciona assim para criar um dicionario
# people = dict()

print(type(people))
print(people["name"])

#people_2 = dict(name="Luiz Otavio", surname="Miranda")
#print(people_2, type(people_2))

# Para acessar algum atributo eu uso os mesmos colchetes dos índices, porém ao inveés de passar
# um valor numérico eu passo a chave.

print(people["height"])
print("===================")
for key in people:
    # Coletando a chave e o valor dela
    print(key, people[key])



# Adicionando uma chave a um dicionario de forma manual

# A chave "Pet" não existe

people["Pet"] = "Dog"

print(people["Pet"])


# Podemos usar ainda chaves dinâmicas

key = "Programa de TV"
people[key] = "Sons Of Anarchy"
print(people[key])

people[key] = "Twin Peaks"

print(people[key])

# Deletando uma chave do dicionário junto com o seu valor
print(people)
del people["Pet"]
print(people)

# Se por acaso estivermos verificando uma chave que não existe ou fazer ua condicional de uma chave
# inexistente

if people.get("Pet"):
    print(people["Pet"])

# Para contornar o problema logo acima, podemos usar o try-except ou usar o método GET dos dicionários

people["Pet"] = "Crocodile"

if people.get("Pet") is None:
	print("Não existe")
else:
    print(people["Pet"])




