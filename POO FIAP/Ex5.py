'''

1. Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. 
2. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. 
3. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. 
4. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

'''

class Pessoa():
    
    def __init__(self, nome = "", idade = 0, profissao = "Desempregado"):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f" Nome: {self.nome}, Idade: {self.idade} anos, e Profissão: {self.profissao}"

    def fez_aniversario(self):
        self.idade += 1
        return f"Parabéns! sua idade agora é {self.idade}"
    
    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá! É um prazer ver um(a) {self.profissao} por aqui!'
        else:
            return f'Olá! É um prazer ver você por aqui!'


# Criando 3 instâncias da classe Pessoa
pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22)

# Imprimindo informações iniciais
print("Informações Iniciais:")
print(pessoa1)
print(pessoa2)
print(pessoa3)

# Utilizando o método de instância aniversario para aumentar a idade de uma pessoa
pessoa1.fez_aniversario()
pessoa3.fez_aniversario()

# Imprimindo informações após aniversário
print("Informações após aniversário:")
print(pessoa1)
print(pessoa3)

# Utilizando o método de classe saudacao para exibir mensagens personalizadas
print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)