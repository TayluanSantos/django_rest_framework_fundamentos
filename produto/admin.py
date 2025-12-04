from django.contrib import admin
from produto.models import Produto

# Registrando o model no Admin
# É possível utilizar o ModelAdmin para maior detalhamento dos campos 
admin.site.register(Produto)
