from marzullo import marzullo_algorithm
import unittest

class testMarzullo(unittest.TestCase):

        
    def testNingunaEntrada(self):
        self.assertEqual( marzullo_algorithm(()), (0,0) )
        
    def testMaximoDePuestos(self):
        
        self.assertEqual( marzullo_algorithm( ( 
                                               (8,12), (11,13), (10,12), (9,12), (7,12), (10,12), (7,12),
                                               (9,15), (10,18), (11, 14)
                                               ) ), (11,12) )
 
    if __name__ == "__main__":
        unittest.main()