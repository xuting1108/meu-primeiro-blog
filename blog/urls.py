#Aqui, estamos importando do Django a função url e todas as nossas views do aplicativo blog. 
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

#Como você pode ver, estamos agora atribuindo uma view chamada post_list à URL raiz. Este padrão de URL corresponde a uma sequência de caracteres vazia, e o resolvedor de URLs do Django irá ignorar o nome de domínio (ou seja, http://127.0.0.1:8000 /) que antecede o caminho completo da URL. Este padrão dirá ao Django que views.post_list é o lugar correto aonde ir se alguém entra em seu site pelo endereço 'http://127.0.0.1:8000 /'.

#A última parte, name='post_list', é o nome da URL que será usado para identificar a view. Pode ser o mesmo nome da view, mas também pode ser algo completamente diferente. Nós vamos usar URLs nomeadas mais à frente, então é importante nomearmos agora todas as URLs de nossa aplicação. Também devemos fazer com que os nomes das URLs sejam únicos e fáceis de lembrar.