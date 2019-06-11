import unittest
from pangram import is_pangram


class PangramTestCase(unittest.TestCase):
    def test_basic(self):
        sentence = 'The quick brown fox jumps over the lazy dog.'
        self.assertEqual(True, is_pangram(sentence))

    def test_basic2(self):
        sentence = 'Two driven jocks help fax my big quiz'
        self.assertEqual(True, is_pangram(sentence))

    def test_basic_negative(self):
        sentence = 'The quick brown fo jumps over the lazy dog.'
        self.assertEqual(False, is_pangram(sentence))

    def test_basic2_negative(self):
        sentence = 'Two driven jocks hel fax my big quiz'
        self.assertEqual(False, is_pangram(sentence))


if __name__ == '__main__':
    unittest.main()
