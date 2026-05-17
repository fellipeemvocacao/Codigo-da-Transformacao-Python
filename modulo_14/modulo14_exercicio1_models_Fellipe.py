from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Produto")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_digits=2, verbose_name="Preço")
    quantidade = models.IntegerField(default=0, verbose_name="Quantidade em Estoque")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return self.nome