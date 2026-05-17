from django.test import TestCase
from django.urls import reverse
from .models import Produto

class ProdutoModelTest(TestCase):

    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Teclado Mecânico",
            descricao="Teclado RGB Switch Blue",
            preco=250.00,
            estoque=10
        )

    def test_criacao_produto_com_valores_corretos(self):
        self.assertEqual(self.produto.nome, "Teclado Mecânico")
        self.assertEqual(self.produto.preco, 250.00)
        self.assertEqual(self.produto.estoque, 10)

    def test_string_representation(self):
        self.assertEqual(str(self.produto), self.produto.nome)


class ProdutoViewTest(TestCase):

    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Mouse Gamer",
            preco=120.00,
            estoque=5
        )

    def test_lista_produtos_view(self):
        response = self.client.get(reverse('lista_produtos')) 
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mouse Gamer")