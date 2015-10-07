#
# Functions to work with edit distance between two strings
#

def isInEditDistance(str1, str2, distance):
	"""return true if edit distance between str1 and str2 is less or equal to distance"""
	dist = 0
	for c1, c2 in zip(str1, str2):
		if c1 != c2:
			dist += 1 
			if dist > distance: 
				return False
	return True
