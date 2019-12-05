import unittest 
#import th unit test package and functions we wa 


from sqrt import newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt


class SqrtTests(unittest.TestCase):
    """Obligatory docstring, test square root functions!"""
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)
        
    def test_sqrt4(self):
         self.assertEqual(builtin_sqrt(4), 2) 
    
if __name__ == '__main__':
    unittest.main()

