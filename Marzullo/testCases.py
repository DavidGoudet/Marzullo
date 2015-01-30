from marzullo import marzullo_algorithm
import unittest

class testMarzullo(unittest.TestCase):

        
    def testNoEntry(self):
        self.assertTrue( marzullo_algorithm(()) )
        
    def testMaxParking(self):
        
        self.assertTrue( marzullo_algorithm( ( 
                                                (8,12), (11,13), (10,12), (9,12), (7,12), (10,12), (7,12),
                                                (9,15), (10,18), (11, 14)
                                                ) )  )
        
    def testMaxHourMinHour(self):
        
        self.assertTrue( marzullo_algorithm( ( 
                                                (6,18),
                                                ) )  )
        
    def testStartEqualToEnd(self):
        
        self.assertTrue( marzullo_algorithm( ( 
                                                (15,15),
                                                ) )  )
        
    def testFullParking(self):
        
        self.assertFalse( marzullo_algorithm( ( 
                                                (8,12), (11,13), (10,12), (9,12), (7,12), (10,12), (7,12),
                                                (9,15), (10,18), (11, 14), (9,13)
                                                ) )  )
        
    def testStartAfterEnd(self):
        
        self.assertFalse( marzullo_algorithm( ( 
                                                (15,12),
                                                ) )  )
 
if __name__ == "__main__":
    unittest.main()
