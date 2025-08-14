from django.contrib import admin
from .models import Movimento, Usuario, Produto, Venda, Entrada, Setor

# Register your models here.
admin.site.register(Movimento)
admin.site.register(Usuario)
admin.site.register(Produto)
admin.site.register(Venda)
admin.site.register(Entrada)
admin.site.register(Setor)
