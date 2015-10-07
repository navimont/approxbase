# Read input file of the format
# <base pairs> <neuron id>
#
# Find all base pairs that differ by not more than MAX_DISTANCE from each other and collect the corresponding ID's
#
# https://github.com/navimont/approxbase/
# Stefan Wehner (Oct 2015)

import sys
import collapse
import edit_distance


# check input parameters
if len(sys.argv) < 2:
	print "specify input file"
inputFile = sys.argv[1]

MAX_DISTANCE = 1


def addToApproxBp(newId, newBasePair, basePairsToIdsTupleList):
	"""
	Method reads from and adds to the input parameter basePairsToIdsTupleList
	basePairsToIdsTupleList consists of tuples of two lists:
	index 0: list of base pairs, each of those has a maxDis edit distance 
	         to any other base pait in this list
	index 1: list of neuron ids
	"""
	for basePairsToIdsTuple in basePairsToIdsTupleList:
		basePairs = basePairsToIdsTuple[0]
		ids = basePairsToIdsTuple[1]
		# MAX_DISTANCE +1 because we may start out with a mutated sequence
		if len(basePairs) > 0 and edit_distance.isInEditDistance(newBasePair,basePairs[0],MAX_DISTANCE+1):
			basePairs.append(newBasePair)
			ids.append(newId)
			return
	basePairsToIdsTupleList.append(([newBasePair],[newId]))


# result structure: base pairs to id's list
bps_ids_tuples_list = []

# process input file
for line in open(inputFile):
	id = line.split()[0]
	bp = line.split()[1]
	addToApproxBp(id, bp, bps_ids_tuples_list)

# collapse list of base pairs and print results

# print format 1: print base pair followed by all neuron Id's
for bps_ids_tuple in bps_ids_tuples_list:
	collapsedBp = collapse.collapseApproximateSequences(bps_ids_tuple[0], 'n')
	print collapsedBp, bps_ids_tuple[1] 
	print
exit(0)

# print format 2: print like input file with the base pairs being replaced with the collapsed version
for bps_ids_tuple in bps_ids_tuples_list:
	collapsedBp = collapse.collapseApproximateSequences(bps_ids_tuple[0], 'n')
	for id in bps_ids_tuple[1]:
		print id,collapsedBp




