import sys

# result structure: base pairs to id's list
bps_ids_list = []

# check input parameters
if len(sys.argv) < 2:
	print "specify input file"

inputFile = sys.argv[1]

maxDist = 1
if len(sys.argv) > 2:
	maxDist = sys.argv[2]
if maxDist not in (1,2):
	print "maximum edit distance between base pair must be 1 or 2"


def editDistance(a, b):
	"""return edit distance between a and b"""
	dist = 0
	for ac, bc in zip(a,b):
		if ac != bc:
			dist += 1 
	return dist


def addToApproxBp(newId, newBasePair):
	"""add new Id and base pair to the existing list
	The list contains of tuples of two lists:
	index 0: list of base pairs, each of those has a maxDis edit distance 
	         to any other base pait in this list
	index 1: list of neuron ids
	"""
	for bps_ids in bps_ids_list:
		for bp in bps_ids[0]:
			if editDistance(newBasePair,bp)	> maxDist:
				break
			bps_ids[0].append(newBasePair)
			bps_ids[1].append(newId)
			return
	bps_ids_list.append(([newBasePair],[newId]))

def collapseBasePairs(basePairList):
	""""""
	collapsedBasePair = ""
	for nucleobases in zip(*basePairList):
		nbFreq = {}
		for nb in nucleobases:
			nbFreq[nb] = nbFreq.get(nb, 0) + 1	
		# find the most frequent nb
		nbDominant = nb
		maxFrequency = nbFreq[nb]
		for nb,freq in nbFreq.iteritems():
			if freq > maxFrequency:
				nbDominant = nb
				maxFrequency = freq	
		collapsedBasePair += nbDominant
	return collapsedBasePair

# process input file
for line in open(inputFile):
	id = line.split()[0]
	bp = line.split()[1]
	addToApproxBp(id, bp)

# collapse list of base pairs and print results
for bps_ids in bps_ids_list:
	collapsedBp = collapseBasePairs(bps_ids[0])
	for id in bps_ids[1]:
		print collapsedBp,id




