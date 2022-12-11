idades = [34,68,38,65,32,19] #lista idades

idade_ano_que_vem = []
for idade in idades:
  idade_ano_que_vem.append(idade + 1)

idade_ano_que_vem = [idade+1 for idade in idades]

idade_maiores_21 = [idade for idade in idades if idade > 21]

# problemas da mutabilidade
# função pode alterar elementos da lista sem o conhecimento do usuario
def faz_processamento_de_visualizacao(lista):
  print(len(lista))
  lista.append(13)

faz_processamento_de_visualizacao(idades)
idades

# boa pratica em vez de usar
# lista = list ou []
# recebe None pois lista é sempre
def faz_processamento_de_visualizacao(lista = list()):
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
    lista = list()
  print(len(lista))
  print(lista)
  lista.append(13)

faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()
faz_processamento_de_visualizacao()

"""# Objetos próprios"""

class ContaCorrente:
  
  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

  def deposita(self, valor):
    self.saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposita(500)

conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)

contas = [conta_do_gui, conta_da_dani]
for conta in contas:
  print(conta)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]

# polimorfismo ou duck type, so é importante ter o atributo
# para poder usar
def deposita_para_todas(contas):
  for conta in contas:
    conta.deposita(100)

contas.insert(0,76) # lista nao se preoculpa com o tipo

print(contas[0], contas[1], contas[2])

guilherme = ('Guilherme', 37, 1981) # tupla
daniela = ('Daniela', 31, 1987)

"""# Herança e polimorfismo"""

from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  @abstractmethod
  def passa_o_mes(self):
    pass

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):
  
  def passa_o_mes(self):
    self._saldo -= 2
    
class ContaPoupanca(Conta):
  
  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

class ContaInvestimento(Conta):
  pass

ContaInvestimento(764)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
  conta.passa_o_mes() # duck typing
  print(conta)

class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    return self._codigo == outro._codigo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

# Para essa igualdade poder ser vericada temos que
# imlementar o metodo __eq__ na classe
conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
conta1 == conta2

conta1 != conta2

conta1 in [conta2]

conta2 in [conta1]

class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
conta1 == conta2

conta1.deposita(10)

conta1 == conta2

class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)

conta1 == conta2
# verifica se é da mesma instancia ou mae da instancia
isinstance(ContaCorrente(34), ContaCorrente)

isinstance(ContaCorrente(34), Conta) #True
# ContaCorrente é filha de conta
idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
  print(i, idades[i])

range(len(idades)) # lazy...

enumerate(idades) # lazy

list(range(len(idades))) # forcei a geração dos valores

list(enumerate(idades))

for indice, idade in enumerate(idades): # unpacking da nossa tupla
  print(indice, "x", idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # ja desempacotando
  print(nome)

for nome, _, _ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)

idades

sorted(idades)

15 < 32

list(reversed(idades))

sorted(idades, reverse=True)

list(reversed(sorted(idades)))

idades

idades.sort()

idades

15 < 32

nomes = ["guilherme", "Daniela", "Paulo"]
sorted(nomes)

class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in contas:
  print(conta)

sorted(contas)

conta_do_guilherme < conta_da_daniela

def extrai_saldo(conta):
  return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
  print(conta)

from operator import attrgetter

for conta in sorted(contas, key=attrgetter("_saldo")):
  print(conta)

conta_do_guilherme < conta_da_daniela

class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def __lt__(self, outro):
    return self._saldo < outro._saldo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

conta_do_guilherme < conta_da_daniela

conta_do_guilherme > conta_da_daniela

for conta in sorted(contas):
  print(conta)

for conta in sorted(contas,reverse=True):
  print(conta)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
  print(conta)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
  print(conta)

class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def __lt__(self, outro):
    if self._saldo != outro._saldo:
      return self._saldo < outro._saldo
    
    return self._codigo < outro._codigo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas):
  print(conta)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

for conta in sorted(contas):
  print(conta)

conta_do_guilherme < conta_da_daniela

conta_do_guilherme <= conta_da_daniela

from functools import total_ordering

@total_ordering
class ContaSalario:
  
  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0
    
  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False
    
    return self._codigo == outro._codigo and self._saldo == outro._saldo
  
  def __lt__(self, outro):
    if self._saldo != outro._saldo:
      return self._saldo < outro._saldo
    
    return self._codigo < outro._codigo
  
  def deposita(self, valor):
    self._saldo += valor
    
  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

conta_do_guilherme <= conta_da_daniela

conta_do_guilherme <= conta_do_paulo

conta_do_guilherme < conta_do_guilherme

conta_do_guilherme == conta_do_guilherme

conta_do_guilherme <= conta_do_guilherme