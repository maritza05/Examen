import unittest
from Prueba06 import Prueba06


class TestPrueba06(unittest.TestCase):

    def setUp(self):
        self.prueba = Prueba06()

    def test_menores(self):
        lista_prueba = [1, 3, 4, 5, 6, 7]
        lista_result = [1, 3, 4]
        resultado = self.prueba.get_menores(lista_prueba, 5)
        self.assertEqual(lista_result, resultado)

    def test_mayores(self):
        lista_prueba = [2, 3, 4, 6, 8]
        lista_result = [8]
        resultado = self.prueba.get_mayores(lista_prueba, 6)
        self.assertEqual(lista_result, resultado)

    def test_get_iguales(self):
        lista_prueba = [3, 6, 9, 9, 12]
        lista_result = [9, 9]
        resultado = self.prueba.get_iguales(lista_prueba, 9)
        self.assertEqual(lista_result, resultado)

    def test_multiplos(self):
        lista_prueba2 = [1, 4, 5, 10, 15, 20]
        lista_result = [5, 10, 15, 20]
        resultado = self.prueba.get_multiplos(lista_prueba2, 5)
        self.assertEqual(lista_result, resultado)

if __name__ == '__main__':
    unittest.main()
