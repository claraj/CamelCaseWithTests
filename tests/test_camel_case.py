import unittest

import camelcase



class TestCamelCase(unittest.TestCase):

    def test_split(self):

        words = camelcase.split("I am a sentence")
        self.assertTrue(len(words), 4)

        words = camelcase.split('And another sentence')
        wordlist = ['And', 'another', 'sentence']
        self.assertEqual(words, wordlist)


        words = camelcase.split('Lots of spaces in     sentence')
        wordlist = ['Lots', 'of', 'spaces', 'in', 'sentence']
        self.assertEqual(words, wordlist)

        words = camelcase.split('   beginning spaces     ')
        wordlist = ['beginning', 'spaces']
        self.assertEqual(words, wordlist)



    def test_first_word(self):

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
               'zEbRa': 'zebra'}

        for wordInput in io:
            self.assertEqual(camelcase.camelcase_word(wordInput), io[wordInput])

