from collections.abc import MutableSequence #classe abstrata - 
# garantir implementação
from numbers import Real #classe abstrata

class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self.like = 0
    
    def dar_like(self):
        self.like += 1
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novo_nome):
        self._nome = novo_nome.title()
   
        
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Filme:{self.nome} - {self.duracao} min - {self.like} likes'

    
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas  = temporadas

    def __str__(self):
        return f'Serie:{self.nome} - {self.temporadas} tmp - {self.like} likes'



vingadores = Filme('vingadores',2018,120)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

nao_nao_olhe = Filme('Não! Não Olhe!',2022,130)
nao_nao_olhe.dar_like()
nao_nao_olhe.dar_like()

wandinha = Serie('Wandinha', 2022, 1)
wandinha.dar_like()
wandinha.dar_like()
wandinha.dar_like()

the_100 = Serie('the 100', 2014, 7)
the_100.dar_like()
the_100.dar_like()
the_100.dar_like()
the_100.dar_like()
the_100.dar_like()

class Playlist(MutableSequence):
    def __init__(self):
        self.__lista = []

    def __delitem__(self, key):
        del self.__lista[key]

    def __getitem__(self, item):
        return self.__lista[item]
    
    def __len__(self):
        return len(self.__lista)

    def __setitem__(self, key, value):
        self.__lista[key] = value

    def insert(self, index, value):
        self.__lista.insert(index, value)

vistos_em_2022 = Playlist()
vistos_em_2022.append(vingadores)
vistos_em_2022.append(nao_nao_olhe)
vistos_em_2022.append(wandinha)
vistos_em_2022.append(the_100)

for i in vistos_em_2022:
    print(i)


