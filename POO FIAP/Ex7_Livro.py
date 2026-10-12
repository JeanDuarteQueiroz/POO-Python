'''

Exercícios

1. Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.

2. Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro. 
    Crie duas instâncias da classe Livro e imprima essas instâncias.

3. Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
    Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

4. Adicione um método estático chamado verificar_disponibilidade à classe Livro
    que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

5. Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

6. No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.

7. No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.

8. Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e
    exiba a mensagem formatada utilizando o método str.

'''

#1. 
class Livro:
    def __init__(self, titulo, autor, ano_pub):
        self._titulo = titulo
        self._autor = autor
        self._ano_pub = ano_pub
        self._disponivel = True
    
    #2.
    def __str__(self):
        return f"\nTítulo da obra: {self.titulo} | Autor da obra: {self.autor} | Ano de Publicação: {self._ano_pub}";
    
    #3.
    def emprestar (self):
        if self._disponivel == True:
            self._disponivel = False
            return f"O Livro {self._titulo} foi emprestado!" 
        else:
            return f" Livro indisponível para empréstimo!"

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro._titulo for livro in Livro.livros if livro._ano_pub == ano and livro._disponivel == True]
        return livros_disponiveis
#2.
livro1 = Livro("Senhor dos Aneis", "J.R.R Tolkien", 1995);
livro2 = Livro("The Witcher", "Autor Desconhecido", 2000);

Livro.livros = [livro1, livro2]  # Adicionando os livros à lista de livros