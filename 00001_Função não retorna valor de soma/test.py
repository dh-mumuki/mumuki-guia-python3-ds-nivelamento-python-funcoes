class Test(unittest.TestCase):

  def positivos(self):
    self.assertAlmostEqual(soma(2, 3), 5)
