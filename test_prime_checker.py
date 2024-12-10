import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_prime(self):
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))
    
    def test_not_prime(self):
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))
    
    def test_edge_cases(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))

if __name__ == "__main__":
    unittest.main()
