import unittest

class TestFile(unittest.TestCase):
    def test_equal(self):
        self.assertEquals("A", "A") 


if __name__ == '__main__':
    unittest.main()