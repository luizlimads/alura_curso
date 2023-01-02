###1

Modificando exibicção django-admin, criar uma classe para exibicao

class ListandoCoisas(admin.ModelAdmin):
    model = 'Coisas'
    list_display = ('id','nome','categoria')
    list_display_links = ('id','nome')
ist_display_links = ('id','nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 2

admin.site.register(Receita,ListandoCoisas)

nome, categoria tem que estar listadas no arquivo models de coisa

###2
Criando novo app 

#py ./manage.py creatapp nome2_app

Preciso adicionar o app em nome_projeto/settings.py
INSTALLED_APPS = [
	'nome2_app',
	.
	.
	.
	]

criar modelo para no arquivo nome2_app/model.py
class Pessoas(models.Model):
	nome = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

	def __str__(self):
		retur self.mome

#py ./manage.py makemigrations
#py ./manage.py migrate


e fazer aparecer no django admin, no arquivi nome2_app/admin
class ListandoPessoas(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome','email')
    list_per_page = 2




relacionamento entre classe Django models.ForeignKey()
class que vai receber a ForeignKey
class recebe_foreign_key(models.Model):
	recebe = models.ForeignKey(modelo_que_tem_a_chave, on_delete= models.CASCADE)
	.
	.
	.
Feito a alteração é necesario fazer as migracoes outra vez
#py ./manage.py makemigrations
#py ./manage.py migrate


admin.site.register(Pessoas, ListandoPessoas)    


###3
campos booleanos > models.BooleanField(default=False)
editar campos direto no admin > list_editable = ('campo',)
ordenação no arquivo view.py ....objects.order_by('date_receita').filter(publicada = True)
upload de imagem > models.ImageField() / é necessario instalar o pilow e fazer alteracoes no nome_projeto/settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

###4
Adicionando imagem para usar o caminho do passo 3 é necessario alterar o arquivo nome_projeto/urls

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    .
    .
    .
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

Implementando busca com o form no index.html
criar um rota no urls.py > urlpatterns = [path('buscar', views.buscar, name='buscar')]
criar um view no views.py >
def buscar(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada = True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)
    
    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'buscar.html', dados)

alterar html para exibir resultado de busca
<form action="{% url 'buscar' %}">
	<input type="text" name="buscar" placeholder="O que está procurando...">
	<button type="submit"><i class="fa fa-search" aria-hidden="true"></i></button>
</form>