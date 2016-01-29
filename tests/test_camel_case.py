import unittest

import camelcase



class TestCamelCase(unittest.TestCase):

    def test_split(self):

        # Correct number of words?
        words = camelcase.split("I am a sentence")
        self.assertTrue(len(words), 4)

        # Are they being turned into a list?
        words = camelcase.split('And another sentence')
        wordlist = ['And', 'another', 'sentence']
        self.assertEqual(words, wordlist)

        # What about sentences with extra spaces?
        words = camelcase.split('Lots of spaces in     sentence')
        wordlist = ['Lots', 'of', 'spaces', 'in', 'sentence']
        self.assertEqual(words, wordlist)

        # Or spaces at the start and end
        words = camelcase.split('   beginning spaces     ')
        wordlist = ['beginning', 'spaces']
        self.assertEqual(words, wordlist)




    def test_first_word(self):

        # Dictionary of input with expected output

        io = {'word': 'word',
              'zebra': 'zebra',
              'ZEBRA': 'zebra',
              'zEBRA': 'zebra',
              'zEbRa': 'zebra'}

        for wordInput in io:
            self.assertEqual(camelcase.first_word(wordInput), io[wordInput])



    def test_camelcase_word(self):

        io = { 'word': 'Word',
               'zebra': 'Zebra',
               'ZEBRA': 'Zebra',
               'zEBRA': 'Zebra',
               'zEbRa': 'Zebra'}

        for wordInput in io:
            self.assertEqual(camelcase.camelcase_word(wordInput), io[wordInput])


    def test_valid_sentence(self):

        # These should be valid
        self.assertTrue(camelcase.valid_sentence("This is a sentence"))
        self.assertTrue(camelcase.valid_sentence("I AM A SENTENCE"))
        self.assertTrue(camelcase.valid_sentence("word"))

        # These should not be valid. Can you fix the validate method so this test passes?
        self.assertFalse(camelcase.valid_sentence("I'm a sentence"))  # Banned character
        self.assertFalse(camelcase.valid_sentence("Hyphens are banned-in variable names"))  # Banned character
        self.assertFalse(camelcase.valid_sentence('No "quotes" in variable names'))  # Banned character
        self.assertFalse(camelcase.valid_sentence("99 unit tests on a shelf"))  # Can't start with number


