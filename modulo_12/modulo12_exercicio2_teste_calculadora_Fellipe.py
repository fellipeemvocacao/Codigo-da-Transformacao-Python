import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()
    def test_soma_valores_positivos(self):
        self.assertEqual(self.calc.somar(10, 5), 15)
    def test_soma_valores_negativos(self):
        self.assertEqual(self.calc.somar(-3, -7), -10)
    def test_divisao_exata(self):
        self.assertEqual(self.calc.dividir(10, 2), 5)
    def test_divisao_resultado_ponto_flutuante(self):
        self.assertEqual(self.calc.dividir(5, 2), 2.5)

    def test_divisao_por_zero_deve_lancar_erro(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

if __name__ == '__main__':
    unittest.main()