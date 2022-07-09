import unittest
import app

class test_num(unittest.TestCase):
  def test_odd_even_1(self):
     self.assertEqual(app.Zen(4),"even","equal")

  def test_odd_even_2(self):
    self.assertEqual(app.Zen(5),"even","notequal")
if __name__ == '__main__':
    unittest.main()   