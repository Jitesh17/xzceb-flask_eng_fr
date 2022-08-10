import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslator(unittest.TestCase):
    
    def test_englishToFrench(self):
        for x, y in [(None, None), ('Hello', 'Bonjour')]:
            self.assertEqual(englishToFrench(x), y)
        for x, y in [('Hello', 'au revoir')]:
            self.assertNotEqual(englishToFrench(x), y)

    def test_frenchToEnglish(self):
        for x, y in [(None, None), ('Bonjour', 'Hello')]:
            self.assertEqual(frenchToEnglish(x), y)
        for x, y in [('au revoir', 'Hello')]:
            self.assertNotEqual(frenchToEnglish(x), y)

if __name__ == '__main__':
    unittest.main()