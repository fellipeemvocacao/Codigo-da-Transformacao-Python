import unittest
from matematica import somar

class TestSoma(unittest.TestCase):

    def test_soma_numeros_positivos(self):
        self.assertEqual(somar(2, 3), 5)

    def test_soma_numeros_negativos(self):
        self.assertEqual(somar(-1, -1), -2)

    def test_soma_com_zero(self):
        self.assertEqual(somar(5, 0), 5)

if __name__ == '__main__':
    unittest.main()