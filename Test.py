import unittest
from Contador import Contador

class TestContador(unittest.TestCase):
    def test1(self):
        '''
        Este test comprueba que el constructor está recibiendo todos los parámetros
        '''
        contador = Contador(5, 2, 2)
        self.assertEqual(contador.valorLimite, 5)
        self.assertEqual(contador.valorInicial, 2)
        self.assertEqual(contador.valorIncremento, 2)

    def test2(self):
        '''
        Este test comprueba que si no se indaca nada, el valor inicial y el incremento
        se inicializarán a 0 y a 1, respectivamente
        '''
        contador1 = Contador(valorLimite = 5)
        self.assertEqual(contador1.valorInicial, 0)
        self.assertEqual(contador1.valorIncremento, 1)
        self.assertEqual(contador1.valorLimite, 5)

    def test3(self):
        '''
        Comprobación de los valores
        '''
        contador2 = Contador(valorLimite = 5)
        contador2.__valorIncial = 1
        self.assertEqual(contador2.getValorInicial(), 0)
        self.assertEqual(contador2.getValorIncremento(), 1)
        self.assertEqual(contador2.getValorLimite(), 5)

if __name__=="__main__":
    unittest.main()
    