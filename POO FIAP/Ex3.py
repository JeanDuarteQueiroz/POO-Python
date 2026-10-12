'''
    Refatorando o seguinte código:
    
    class Musica:
    Nome = ""
    Artista = ""
    Estilo = ""
    
    Musica = Musica()
    Musica.Nome = "Desaguar"
    Musica.Artista = "7 Minutos"
    Musica.Estilo = "Rap Geek"

    print(f" A música {Musica.Nome}, do artista {Musica.Artista} tem o seguinte estilo: {Musica.Estilo}");

    Usando  construtores e métodos
'''

class Musica:
    
    musicas_ativas = []
    
    def __init__(self, nome, autor, categoria):
        self.nome = nome
        self.autor = autor
        self.categoria = categoria
        Musica.musicas_ativas.append(self)
    
    def __str__(self):
        return f"Nome: {self.nome} | Autor: {self.autor} | Categoria: {self.categoria}\n"
    
    def listar_musicas():
        print(f"Lista de Musicas:");
        for musica in Musica.musicas_ativas:
            print(f"Nome: {musica.nome} | Autor: {musica.autor} | Categoria: {musica.categoria}")

Musica1 = Musica("Desaguar", "7 Minutoz", "Rap Geek")
Musica2 = Musica("Rap do Itachi", "7 Minutoz", "Rap Geek")

Musica.listar_musicas()