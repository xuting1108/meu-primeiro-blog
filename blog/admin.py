from django.contrib import admin
from .models import Post

#Para tornar nosso modelo visível na página de administração
admin.site.register(Post)

