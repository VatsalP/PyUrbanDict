import unittest
from pyurbandict import main


class ModelTest(unittest.TestCase):
    def test_get_data(self):
        m = main.Model('potato')
        self.assertEqual(200, m.status)


if __name__ == '__main__':
    unittest.main()
