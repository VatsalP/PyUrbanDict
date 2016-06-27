import unittest

import pyurbandict
from pyurbandict.main import Word, Random
from pyurbandict.exception import KeywordError


class WordTest(unittest.TestCase):
    def test_connectivity(self):
        m = Word('potato')
        self.assertEqual(200, m.status_code)

    def test_exists(self):
        m = Word('potato')
        self.assertEqual(True, m.exists)

    def test_not_exists(self):
        m = Word('skndlasnikdjbksad')
        self.assertEqual(False, m.exists)

    def test_get_tags(self):
        m = Word('potato').get_tags()
        self.assertEqual(list, type(m))

    def test_get_definitions(self):
        m = Word('potato').get_definitions()
        self.assertEqual(list, type(m))

    def test_get_sound(self):
        m = Word('potato').get_sound()
        self.assertEqual(list, type(m))

    @unittest.expectedFailure
    def test_keyword_none(self):
        keyword = None
        with self.assertRaises(KeywordError):
            Word()

class RandomTest(unittest.TestCase):
    def test_get_random(self):
        n = Random().get_random()
        self.assertEqual(list, type(n))

if __name__ == '__main__':
    unittest.main()
