import unittest

from age import categorize_by_age

class TestSubCase(unittest.TestCase):
    def test_child(self):
        for age in range(0, 10):
            with self.subTest():
                self.assertEqual(categorize_by_age(age), "Child")          
                print(f'{age} is considered as Children.')
                        
    def test_adult(self):
        for age in range(19, 66):
            with self.subTest():
                self.assertEqual(categorize_by_age(age), "Adult")          
                print(f'{age} is considered as Adult.')
    
    def test_golden_age(self):
        for age in range(66, 151):
            with self.subTest():
                self.assertEqual(categorize_by_age(age), "Golden age")          
                print(f'{age} is considered as Golden Age.')

                    
if __name__ == "__main__":
    unittest.main(verbosity=2)