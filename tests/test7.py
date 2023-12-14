import unittest

from src.main import longest_chain


class TestLongestChain(unittest.TestCase):
    def test_empty_input(self):
        result = longest_chain([])
        self.assertEqual(result, 0)

    def test_single_word(self):
        words = ['test']
        result = longest_chain(words)
        self.assertEqual(result, 1)

    def test_max_chain(self):
        words = ['abcd', 'abc', 'ab', 'a', 'bcde', 'bcd']
        result = longest_chain(words)
        self.assertEqual(result, 4)

    def test_words_with_different_lengths(self):
        words = ['cat', 'cats', 'at', 'rate', 'crate']
        result = longest_chain(words)
        self.assertEqual(result, 3)

    def test_invalid_word_format(self):
        words = ['abc', 'test*', '123']
        result = longest_chain(words)
        self.assertEqual(result, 1)

    def test_all_words_are_single_character(self):
        words = ['a', 'b', 'c', 'd']
        result = longest_chain(words)
        self.assertEqual(result, 1)

    def test_max_word_length(self):
        long_word = 'a' * 50
        words = [long_word]
        result = longest_chain(words)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()
