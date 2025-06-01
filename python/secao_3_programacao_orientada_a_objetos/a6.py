class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'

# Relacionando escritor e caneta (ASSOCIAÇÃO)

escritor = Escritor('Arthur Conan Doyle')
caneta = FerramentaDeEscrever('Caneta')
maquina = FerramentaDeEscrever('Máquina')

# LINKANDO OS DOIS OBJETOS
escritor.ferramenta = maquina

print(caneta.escrever())
print(maquina.escrever())
print(escritor.ferramenta.escrever())


print("===================================================================")


class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([produto.preco for produto in self._produtos])

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()

    # empacotando
    def inserir_produto(self, *produtos):
        # Três formas iguais de inserir o produto
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = CarrinhoDeCompras()
p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

carrinho.inserir_produto(p1, p2)

carrinho.listar_produtos()

print("=================================================================================")

# COMPOSIÇÃO

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserirEndereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserirEnderecoExterno(self, endereco):
        self.enderecos.append(endereco)

    def listarEnderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print("Apagando: ", self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print("APAGANDO", self.rua, self.numero)


cliente1 = Cliente("Maria")
cliente1.inserirEndereco("Av Brasil", 54)
cliente1.inserirEndereco("25 Março", 123)


endereco = Endereco("Saudade", 11)
cliente1.inserirEnderecoExterno(endereco)

cliente1.listarEnderecos()

del cliente1

print("ENDDDDDDDDDDDD")













