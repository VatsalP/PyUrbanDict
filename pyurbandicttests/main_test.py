import unittest
from pyurbandict import main


class ModelTest(unittest.TestCase):
    def test_get_data(self):
        m = main.Model('potato')
        data, status = m.get_data()
        self.assertEqual(200, status)


if __name__ == '__main__':
    unittest.main()
