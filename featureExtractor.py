import sys
import os
import csv


def displayUsage():
	string = "\ndnsFeatureExtractor.py\n"
	string += "---------------------------------------"
	string += "\nExtracts features to a csv from a text file of dns query names\n"
	string += "\nInputs: a .txt file where each line is a dns query name\n"
	string += "\nOutputs: a .csv file with column headers of various features used for classification\n"
	string += "usage: python dnsFeatureExtractor.py <input.txt> <output.csv>"
	print(string)

def badArgs(numArgsRequired):
	return len(sys.argv) != numArgsRequired

# ======================================================================================


def main():
	if badArgs(3):
		displayUsage()
		return

	inputFile = sys.argv[1]
	outputFile = sys.argv[2]

	queries = [line.rstrip('\n') for line in open(inputFile)]
	#print(queries)
	lengths = [len(query) for query in queries]
	numDigits = [sum(c.isdigit() for c in query) for query in queries]
	numPeriods = [sum(c == '.' for c in query) for query in queries]
	numDashes = [sum(c == '-' for c in query) for query in queries]
	includesCom = [(1 if ".com" in query else 0) for query in queries]
	includesNet = [(1 if ".net" in query else 0) for query in queries]
	includesOrg = [(1 if ".org" in query else 0) for query in queries]
	includesEdu = [(1 if '.edu' in query else 0) for query in queries]

	#print(queries[:5])
	#print(lengths[:5])
	#print(numDigits[:5])
	#print(numPeriods[:5])
	#print(numDashes[:5])
	#print(includesCom[:5])
	#print(includesNet[:5])
	#print(includesOrg[:5])

	with open(outputFile, mode='w') as outfile:
		output_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
		output_writer.writerow(['query', 'length', 'numDigits', 'numPeriods', 'numDashes', 'includesCom', 'includesNet', 'includesOrg', 'includesEdu'])
		for i in range(len(queries)):
			output_writer.writerow([queries[i], lengths[i], numDigits[i], numPeriods[i], numDashes[i], includesCom[i], includesNet[i], includesOrg[i], includesEdu[i]])







if __name__ == '__main__':
	main()
