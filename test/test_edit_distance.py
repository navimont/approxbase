import unittest

from src import edit_distance

class TestEditDistance(unittest.TestCase):

	def test_editDistance_equal(self):
		self.assertTrue(edit_distance.isInEditDistance("stefan", "stefan", 0))

	def test_editDistance_empty_string(self):
		self.assertTrue(edit_distance.isInEditDistance("", "", 0))

	def test_editDistance_fails(self):
		self.assertFalse(edit_distance.isInEditDistance("stefan", "stepan", 0))

	def test_editDistance_passes(self):
		self.assertTrue(edit_distance.isInEditDistance("stefan", "stepan", 1))

	def test_editDistance_differentLength(self):
		# extra characters are being ignored
		self.assertTrue(edit_distance.isInEditDistance("stefan", "stefan1", 0))



if __name__ == '__main__':
	unittest.main()
