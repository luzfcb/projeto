import unittest
from programa import verifica_igual, faz_algo, soma, subtracao
 
class TestaVerificaIgual(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_numero_3_igual_4(self):
        self.assertEqual( verifica_igual(3,4), True)
 
    def test_numero_3_igual_3(self):
        self.assertEqual( verifica_igual(3,3), True)
    
    def test_soma(self):
        self.assertEqual( soma(3,3), 8)
        
    def test_subtracao(self):
        self.assertEqual( subtracao(10,7), 3)        

class TestaFazAlgo(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_faz_algo_0(self):
        self.assertEqual( faz_algo(), 0)
 
    def test_faz_algo_1(self):
        self.assertEqual( faz_algo(True), 1)
        
    def test_faz_algo_2(self):
        self.assertEqual( faz_algo(True, True), True)        
 
if __name__ == '__main__':
    unittest.main()
