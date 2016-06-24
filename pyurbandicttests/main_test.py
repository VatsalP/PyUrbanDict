import unittest
from pyurbandict import main


class DefinitonTest(unittest.TestCase):
    def test_connectivity(self):
        m = main.Word('potato')
        self.assertEqual(200, m.status_code)

    def test_exists(self):
        m = main.Word('potato')
        self.assertEqual(True, m.exists)

    def test_not_exists(self):
        m = main.Word('skndlasnikdjbksad')
        self.assertEqual(False, m.exists)

    def test_get_tags(self):
        m = main.Word('potato').get_tags()
        self.assertEqual(list, type(m))

    def test_get_definitions(self):
        m = main.Word('potato').get_definitions()
        self.assertEqual(list, type(m))

    def test_get_sound(self):
        m = main.Word('potato').get_sound()
        self.assertEqual(list, type(m))
if __name__ == '__main__':
    unittest.main()
