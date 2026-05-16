import unittest
from calculadora import Calculadora

class TestCalculadoraValidacoes(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_divisao_por_zero_deve_lancar_value_error(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)

    def test_soma_com_entrada_nao_numerica_deve_lancar_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.somar("10", 5)

    def test_divisao_com_entrada_nao_numerica_deve_lancar_type_error(self):
        with self.assertRaises(TypeError):
            self.calc.dividir(10, None)
    
    def test_operacoes_com_valores_extremos_ou_nan(self):
        import math
        resultado = self.calc.somar(float('inf'), 1)
        self.assertTrue(math.isinf(resultado))

if __name__ == '__main__':
    unittest.main()