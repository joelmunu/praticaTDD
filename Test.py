import unittest
import Contador

class TestContador(unittest.TestCase):
    def test1(self):
        '''
        Este test comprueba que el constructor está recibiendo todos los parámetros
        '''
        contador = Contador(5, 2, 2)
        self.assertEqual(contador.valorLimite, 5)
        self.assertEqual(contador.valorInicial, 2)
        self.assertEqual(contador.valorIncremento, 2)