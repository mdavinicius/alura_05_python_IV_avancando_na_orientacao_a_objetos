class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  # o super puxa os atributos da classe Mãe
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} minutos - {self._likes} Likes'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)  # o super puxa os atributos da classe Mãe
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]  # Transformar o Objeto em iterável

    def __len__(self):
        return len(self._programas)


vingadores = Filme('vingadores: guerra infinita', 2018, 160)  # cria um objeto usando a Classe Filme
atlanta = Serie('atlanta', 2018, 2)  # cria um objeto usando a Classe Serie
tmep = Filme('Todo mundo em pânico', 1999, 100)  # cria um objeto usando a Classe Filme
demolidor = Serie('Demolidor', 2016, 2)  # cria um objeto usando a Classe Serie

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
# atribui vários 'likes' para cada filme e série

filmes_e_series = [vingadores, atlanta, demolidor, tmep]  # cria uma lista com eles
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)  # damos um nome e inserimos essa lista na Classe Playlist para criar uma playlist
print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')  # verificando o tamanho da playlist, possui 4 objetos
print("-----------------------------------")

for programa in playlist_fim_de_semana:
    print(programa)
# printando cada um dos objetos contidos na playlist
print("-----------------------------------")

print(f'Tá ou não tá? {vingadores in playlist_fim_de_semana}')
# verificando se um objeto está dentro da playlista, retorna True ou False
print("-----------------------------------")

linux = Programa("Linux", 1980)  # cria um objeto com a classe mãe Programa
print(linux)  # chamando o objeto via __str__
linux.nome = "mac"  # mudando o nome do objeto via @setter
print(linux)
linux.dar_like()  # dando like
print(linux)
print(linux.nome)  # chamando o nome do objeto pela função nome, graças ao @property
print(linux.likes)  # verificando quantos likes o ojbeto tem, outra função com @property, evitando o uso do get