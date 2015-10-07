import unittest

from src import collapse

class TestCollapse(unittest.TestCase):
	placeholder = '_'		

	def test_collapseLetters(self):
		self.assertEqual('a', collapse.dominantLetter(['a', 'a', 'b', 'f', 'a'], self.placeholder))

	def test_collapseLetters_emptyList(self):
		self.assertIsNone(collapse.dominantLetter([], self.placeholder))

	def test_collapseLetters_twoDominantLetters(self):
		self.assertEqual(self.placeholder, collapse.dominantLetter(['a', 'a', 'b', 'c', 'b'], self.placeholder))

	def test_collapseLetters_dominantLetterComesLast(self):
		self.assertEqual('x', collapse.dominantLetter(['a', 'a', 'b', 'c', 'b', 'x', 'x', 'x'], self.placeholder))


	def test_approxSeq(self):
		ancestor = collapse.collapseApproximateSequences(["STEPAN", "STEFAN", "STEFAM", "STEFAN"], self.placeholder)
		self.assertEqual("STEFAN", ancestor)

if __name__ == '__main__':
	unittest.main()
