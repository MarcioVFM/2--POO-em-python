"""
Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
"""

class Livro:
    lista_livros = []

    def __init__(self, titulo, autor, ano_publicado ):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicado = ano_publicado
        self._disponivel = True
        Livro.lista_livros.append(self)

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicado}'

    def emprestar(self):
        if not self._disponivel:
            print('Livro indisponivel')
            return
        self._disponivel = False

    #@staticmethod / COMO EU FIZ
    #def verificar_disponibilidade(ano):
        #for livro in Livro.lista_livros:
            #if ano == livro._ano_publicado:
                #livros_ano = []
                #livros_ano.append(livro)
        #return livros_ano"""

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
        return livros_disponiveis


livro1 = Livro('senhor dos aneis', 'Tolkei', 1900)
livro2 = Livro('Pao', 'Tolkei', 1900)
livro1.emprestar()
print(livro1._disponivel)
livro1.emprestar()
print(Livro.verificar_disponibilidade(1900))


