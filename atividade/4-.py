"""Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo. Inicie o atributo ativo como False por padrão.

Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos. Utilize propriedades, se necessário.

Crie uma instância da classe e imprima o valor da propriedade titular.

Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos desta classe e atribua valores aos seus atributos através do método construtor.

Crie um método de classe para a conta ClienteBanco."""

#1
class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False  

#2
    def __str__(self):
        return f'{self._titular} | {self._saldo}'

#3  
    def ativar_conta(self):
        self._ativo = True

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'desativo'


conta1 = ContaBancaria('Jose', 1000.00)
conta2 = ContaBancaria('Jorge', 3000.00)
print(conta1)
print(conta2)
conta1.ativar_conta()
print(conta1.ativo)
print(f'Dono da conta 1: {conta1._titular}')