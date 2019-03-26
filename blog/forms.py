from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
# Primeiro, precisamos importar o módulo de formulários do Django (from django import forms) e, obviamente, o nosso modelo Post (from .models import Post).

# PostForm, como você já deve suspeitar, é o nome do nosso formulário. Precisamos dizer ao Django que esse form é um ModelForm (pro Django fazer algumas mágicas para nós) – forms.ModelForm é o responsável por essa parte.

# Em seguida, temos a class Meta em que dizemos ao Django qual modelo deverá ser usado para criar este formulário (model = Post).

# Por fim, podemos dizer quais campos devem entrar no nosso formulário. Neste cenário, queremos que apenas o title e o text sejam expostos -- author deve ser a pessoa que está logada no sistema (nesse caso, você!) e created_date deve ser configurado automaticamente quando criamos um post (no código), correto?

# E é isso! Tudo o que precisamos fazer agora é usar o formulário em uma view e mostrá-lo em um template.