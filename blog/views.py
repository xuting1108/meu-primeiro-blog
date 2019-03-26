from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post
#O ponto antes de models significa diretório atual ou aplicativo atual. Tanto views.py como models.py estão no mesmo diretório. Isto significa que podemos usar . e o nome do arquivo (sem py).

def post_detail(request, pk):
	Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
#função (def) chamada post_list que recebe um request, executa a função render que irá renderizar (montar) nosso modelo de acordo com o template blog/post_list.html, e retorna (return) o resultado.
