from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
#função (def) chamada post_list que recebe um request, executa a função render que irá renderizar (montar) nosso modelo de acordo com o template blog/post_list.html, e retorna (return) o resultado.
