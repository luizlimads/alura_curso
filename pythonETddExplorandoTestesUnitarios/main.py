import re
from datetime import date
from dateutil.relativedelta import relativedelta

class Funcionario:
    def __init__(self,nome_completo,data_nascimento,salario):
        self._nome = nome_completo.strip()
        self._data_nascimento = self._padrao_data(data_nascimento)
        self._salario = salario
    
    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
       dia, mes, ano = self._data_nascimento.split('/')
       nascimento = date(day=int(dia),month=int(mes),year=int(ano))
       idade_atual = relativedelta(date.today(),nascimento).years
       return idade_atual
    
    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo
    
    def ultimo_nome(self):
        nome_dividido = self._nome.split()
        return nome_dividido[-1]

    def bonus(self):
        if self._salario <= 1000:
            return self._salario*.1
        else:
            raise Exception('O salário é muito alto para receber bonus')
        pass    

    def _padrao_data(self,data):
        padrao = '([0-9]{2})[/.-]([0-9]{2})[/.-]([0-9]{4})'
        padrao_data = re.match(padrao,data)
        if padrao_data:
            return ('/'.join([padrao_data[i] for i in range(1,4)]))
        else:
            raise ValueError('Data >> dd/mm/aaaa')

    def _eh_socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return (self._salario >= 100000) and (self.ultimo_nome() in sobrenomes)

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
