import unittest
from pyurbandict import main


class ModelTest(unittest.TestCase):
    def test_connectivity(self):
        m = main.Model('potato')
        self.assertEqual(200, m.status_code)

    def test_exists(self):
        m = main.Model('potato')
        self.assertEqual(True, m.exists)

    def test_not_exists(self):
        m = main.Model('skndlasnikdjbksad')
        self.assertEqual(False, m.exists)

    def test_multiword_keyword(self):
        m = main.Model('ayy lmao')
        self.assertEqual(True, m.exists)


if __name__ == '__main__':
    unittest.main()
