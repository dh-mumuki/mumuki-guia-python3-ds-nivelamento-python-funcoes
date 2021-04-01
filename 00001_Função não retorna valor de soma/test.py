import random

class Test(unittest.TestCase):

  def test_somas(self):
    # Soma de positivos
    self.assertAlmostEqual(soma(2, 3), 5)
    self.assertAlmostEqual(soma(1, 2), 3)
    self.assertAlmostEqual(soma(5, 6), 11)
    self.assertAlmostEqual(soma(9, 9), 18)
    
    # Soma de negativos e positivos
    self.assertAlmostEqual(soma(-2, 3), 1)
    self.assertAlmostEqual(soma(1, -2), -1)
    self.assertAlmostEqual(soma(5, -6), -1)
    self.assertAlmostEqual(soma(9, -9), 0)
    
    # Testes aleatórios
    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    self.assertAlmostEqual(soma(a, b), a + b)
    self.assertAlmostEqual(soma(a, b), a + b)
    self.assertAlmostEqual(soma(a, b), a + b)
    self.assertAlmostEqual(soma(a, b), a + b)