Usando pytest framework para automatizar testes em Python

Comandos uteis
	
	pyhon -m venv venv* # cria virtual env con nome venv*

	pip freeze > requeriments.txt # salva dependencias no arquivo requeriments.txt


Para executar pytest é preciso uma pasta na raiz do projeto chamada **tests** dentro da pasta o arquivo __init.py__ e o arquivo de teste chamado __test_nome_escolhido.py__. 

No arquivo test_nome_escolhido.py uma classe chamada test_nome_qualquer e seus metodos serão os testes a fazer.  

Nome dos test's devem ser o mais verboso possivel, mais explicativo possivel

Metodologia de teste Given When then. 

Dado(contexto) Quando(acao) Entao(desfecho)

Metodologia TDD - codigo voltado para testes, ajuda a promover a refatoração do codigo.