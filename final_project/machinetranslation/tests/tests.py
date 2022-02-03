"""Test Module."""
import unittest
import sys

sys.path.insert(0, '/home/project/xzceb-flask_eng_fr/final_project/')

from machinetranslation import translator

class TestEnglishToFrench(unittest.TestCase):
    """Unit test for English-to-French."""

    def test1(self):
        """Unit test 1 English-to-French."""
        self.assertEqual(translator.english_to_french("Hello"), "Bonjour")

    def test2(self):
        """Unit test 2 English-to-French."""
        self.assertEqual(translator.english_to_french(""), "")

class TestFrenchToEnglish(unittest.TestCase):
    """Unit test for French-to-English."""

    def test1(self):
        """Unit test 1 French-to-English."""
        self.assertEqual(translator.french_to_english("Bonjour"), "Hello")

    def test2(self):
        """Unit test 2 French-to-English."""
        self.assertEqual(translator.french_to_english(""), "")

unittest.main()