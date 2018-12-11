import sys
import os
import csv


def displayUsage():
	string = "\ntcp_FeatureExtractor.py\n"
	string += "---------------------------------------"
	string += "\nExtracts features to a csv from a text file of tcp time deltas\n"
	string += "\nInputs: a .txt file where each line is a frame number and tcp time delta\n"
	string += "\nOutputs: a .csv file with column headers of various features used for classification\n"
	string += "usage: python tcp_featureExtractor.py <input.txt> <output.csv>"
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

	queries = [line.rstrip('\n').split() for line in open(inputFile)]
	time_deltas = [item[1] for item in queries]


	#print(queries)

	#print(queries[:5])
	#print(lengths[:5])
	#print(numDigits[:5])
	#print(numPeriods[:5])
	#print(numDashes[:5])
	#print(includesCom[:5])
	#print(includesNet[:5])
	#print(includesOrg[:5])
	print(time_deltas)


	with open(outputFile, mode='w') as outfile:
		output_writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
		output_writer.writerow(['timeDeltas'])
		for i in range(len(time_deltas)):
			output_writer.writerow([time_deltas[i]])

if __name__ == '__main__':
	main()