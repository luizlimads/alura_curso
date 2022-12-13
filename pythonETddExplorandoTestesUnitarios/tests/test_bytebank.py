from main import Funcionario
import pytest
from pytest import mark



class TestClass:
    def test_quando_idade_recebe_01_01_200_deve_retornar_22(self):
        # Metodologia Given-When-Then
        entrada = '01-01-2000' # Given - contexto
        esperado = 22

        funcionario_teste = Funcionario('Test', entrada, 1)   
        resultado = funcionario_teste.idade() # When - acao 

        assert resultado == esperado # Then - desfecho

    def test_quando_nome_recebe_Marcio_Oliveira_deve_retornar_oliveira(self):
        entrada = 'Marcio Oliveira'
        esperado = 'Oliveira'

        funcionario_teste = Funcionario('Marcio Oliveira','01-01-2000',1)
        resultado = funcionario_teste.ultimo_nome()

        assert resultado == esperado

    @mark.bonus
    def test_quando_bonus_recebe_1001_deve_retornar_exception(self):
        with pytest.raises(Exception):      
            entrada = '1001' # Given

            funcionario_teste = Funcionario('test','01-01-2000',entrada)
            resultado = funcionario_teste.bonus() # When

            assert resultado # Then

    def test_retorno_nome(self):
        entrada = 'Marcio Oliveira'
        esperado = 'Marcio Oliveira'

        funcionario_teste = Funcionario(entrada,'01-01-2000',1)
        resultado = funcionario_teste.nome

        assert resultado == esperado

    def test_retorno_salario(self):
        entrada = 1
        esperado = 1

        funcionario_teste = Funcionario('Marcio Oliveira','01-01-2000',entrada)
        resultado = funcionario_teste.salario

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000 #given
        esperado = 90000

        funconario_teste = Funcionario('Paulo Bragança', '11/11/2000', entrada)
        funconario_teste.decrescimo_salario() # when
        resultado = funconario_teste.salario

        assert resultado == esperado  # then



    def test_retorno_str(self):
        nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000  # given
        esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

        funconario_teste = Funcionario(nome, data_nascimento, salario)
        resultado = funconario_teste.__str__() # when

        assert resultado == esperado  # then

