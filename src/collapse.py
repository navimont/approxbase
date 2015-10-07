# 
# Functions for collapsing multiple similar strings into one probable ancestor 
#

def dominantLetter(letters, placeholder):
	"""letters is a list of letters. Return the letter
	that occurs most often in the sequence. 
	If two letters reach the same score, return placeholder instead.
	"""
	letterFreq = {}
	for l in letters:
		letterFreq[l] = letterFreq.get(l, 0) + 1					
	dominantLetter = None
	maxFrequency = 0
	for l,freq in letterFreq.iteritems():
		if freq > maxFrequency:
			dominantLetter = l
			maxFrequency = freq
		elif freq == maxFrequency:
			dominantLetter = placeholder
	return dominantLetter


def collapseApproximateSequences(seqList, placeholder):
	"""Compare letters in sequences at every position of the sequence
	Put up the resulting list of letters for a vote (the most frequent
	letter will win). If there are multiple winners, substitute placeholder.
	seqList is a list of strings, all of the same length.
	"""
	collapsedSequence = ""
	for lettersAtPositionN in zip(*seqList):
		collapsedSequence += dominantLetter(lettersAtPositionN, placeholder)
	return collapsedSequence

