from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):#__init__ e o metodo construtor, que sera iniciado quando utilizar a classe Restaurante
        self._nome = nome.title() #O .title() faz com que a primeira letra de cada palavra seja maiuscula
        self._categoria = categoria.upper()#.upper torna todas as letras pra maiusculo
        self._ativo = False# O _ antes das variaveis e para demostrar que aquele objeto nao e para ser mexidom fora da classe, voce pode, mas nao deve
        self._avaliacao = []
        Restaurante.restaurantes.append(self)


    def __str__(self):#__str__ sera iniciado sempre que um objeto restaurannte for instanciado e saira um print com o texto desejado
        return f'Restaurante {self._nome} de {self._categoria}'

    @classmethod#quando uma funcao va precisa da classe, aqui para pegar a lista de restaurantes da classe Restaurante, usa esse metodo
    def lista_restaurantes(cls):
        print(f'{'Nome Restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliação'.ljust(20)}| Status')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)}| {restaurante.ativo}')

    def alterar_estado(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '✓' if self._ativo else '✕'
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 0
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        media = round(soma_das_notas / len(self._avaliacao) , 1)
        return media