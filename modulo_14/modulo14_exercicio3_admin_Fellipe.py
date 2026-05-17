from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'atualizado_em')
    
    list_filter = ('disponivel', 'criado_em')
    
    search_fields = ('nome', 'descricao')
    
    list_editable = ('preco', 'estoque')