iniciar projeto
django-admin startproject nome_project .

__init__.py diz que o diretorio deve ser considerado um pacote
setting.py configurações relacionadas ao projeto
urls.py todas as urls do projeto devem estar aqui

criar um app 
#manege.py startapp nome_app, no diretori criado no arquivo 'apps.py' o valor de name dever ser colocado no caminho nome_projecto/settings.py na parte installeda_apps[valor_name]

dentro do app criar um arquivo urls.py com o conteudo 
from django.urls import path
from . import views
urlpatterns = [path('', view.index, name='index')]
arquivo views qual url queremos exibir para o cliente dentro do arquivo 


No arquivo nome_app/view.py
from django.http import HttpResponse
def index(request): 
    return HttpResponse('<h1>Hello World!</h1>')

No arquivo nome_projeto/urls.py
from django.urls import path, include
urlpatterns = [path('',include('nome_app.urls')),...]

### 2
inserindo templates
criar pasta templates e os arquivos html 
arquivo nome_app/views.py aterar return para render(request,'index.html')


na pasta projeto/settings.py alterar

templates[
.
.
.
DIRS:[os.path.join(BASE_DIR, 'nome_app/templates')],
.
.
.
]
.
.
.
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'alurareceita/static')
]

no arquivo index deve os de ser colocado no inicio
{% load static %}

a cada novo carregamento de objetos estaticos
{% static 'caminho' %}

###3
criar link
com o caminho no nome_app
dentro do arquivo html
{% url 'name_path' %}

adicionar path em nome_app/urls
path('nome_path',views.nome_path, name='nome_path')

Adicionar em view pagina a ser renderizada
def nome_path(request):
    return render(request,'nome_path.html') # nome_path.html deve estar dentro de templates em nome_app

###4
Gerando visualizacao no html a partir de python, é preciso inserir um contexto na hora de renderizar a pagina

def index(request): 
    receitas = {
        1:'Lasanha',
        2:'Sorvete',
        3:'Suco Verde'
    }
    dados = {
        'nome_das_receitas': receitas
    }
    return render(request,'index.html',dados)

No arquivo html é possivel iterar dentro do contexto dados
{% for chave,valor in nome_das_receitas.items %}

{{chave}} mostrar item na pagina html
{{valor}} 

{% endfor %}


Integrando com o postgres
instalar pacote psycopg2, psycopg2-binary
Configurar defauld bd em nome_projeto/settings.py na parte de DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alura_receita',
        'USER': 'postgres',
        'PASSWORD': '****',
        'HOST': 'localhost'
    }
}

Criar modelo em model dentro de nome_app/model por exemplo
class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)

#py manage.py makemigrations
#py manage.py migrate

###5
django-admin adicionar em nome_app/admin.py
admin.site.register(modelo_criado)

Criar usuario caso nao tenha
#py manage.py createsuperuser



