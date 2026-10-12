'''
    Exercícios:
    
1 - Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.
    Crie uma instância dessa classe e atribua valores aos seus atributos.
    
2 - Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. 
    Instancie um restaurante e atribua valores aos seus atributos.

3 - Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. 
    Crie uma instância utilizando o construtor.

4 - Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. 
    Exiba essa mensagem para uma instância de restaurante.

5 - Crie uma classe chamada Cliente e pense em 4 atributos. 
    Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.

'''
#1.
class Carro():
    modelo = ""
    cor = ""
    ano = ""

carro1 = Carro()
carro1.modelo = "Esportivo"
carro1.cor = "Preto"
carro1.ano = "2026"

#2.
class Restaurante():
    nome = ""
    categoria = ""
    ativo = False
    tamanho = ""
    cor = ""

restaurante1 = Restaurante()
restaurante1.nome = "Pizza Plaza"
restaurante1.categoria = "Fast Food"
restaurante1.tamanho = "Grande"
restaurante1.cor = "Preto"

#3.
class Restaurante():
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        ativo = False
        tamanho = ""
        cor = ""

restaurante2 = Restaurante("Pizza Plaza", "Bistrô")

#4.
class Restaurante():
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        ativo = False
        tamanho = ""
        cor = ""

    def __str__(self):
        return f"Nome: {self.nome} | Categoria: {self.categoria}"
    
restaurante2 = Restaurante("Pizza Plaza", "Bistrô")

print(restaurante2)

#5.
class Cliente:
    
    def __init__(self, nome, idade, tipo, ativo=False):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.ativo = ativo
    
cliente1 = Cliente(
    nome = "Jean",
    idade = "24",
    tipo = "Consumidor Final"
    );
cliente2 = Cliente("Alessandro", "33", "Revenda");
cliente3 = Cliente("Sandra", "23", "Consumidor Final");

print(vars(cliente1))