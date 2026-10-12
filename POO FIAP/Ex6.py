'''

1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. 
    Inicie o atributo ativo como False por padrão.

2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. 
    Crie duas instâncias da classe e imprima essas instâncias.

3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. 
    Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. 
    Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco.

'''

#1.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    #2.
    def __str__(self):
        return f"\nTitular da Conta: {self._titular} | Saldo Atual: {self._saldo} | Status: {self._ativo}"

    #3.
    def ativar_conta (self):
        self._ativo = True
    
    @property
    def titular(self):
        self._titular

    
#2.
conta1 = ContaBancaria("Jean", 100)
conta2 = ContaBancaria("Sandra", 200)
print(conta1, conta2)

#3.
conta1.ativar_conta()
print(conta1, conta2)

#5.
print(conta1._titular)