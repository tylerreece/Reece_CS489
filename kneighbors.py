from sklearn.neighbors import KNeighborsClassifier
import csv
import sys
import os


def displayUsage():
	string = "\nkneighbors.py\n"
	string += "---------------------------------------"
	string += "\nComputes information about k nearest neighbors model from feature data\n"
	string += "\nInputs: a .csv file of dns query name features\n"
	string += "usage: python kneighbors.py <k_value> <input.csv>"
	print(string)

def badArgs(numArgsRequired):
	return len(sys.argv) != numArgsRequired


def splitData(numLines):
	# splits data into training and testing. 
	# returns tuple of (trainingX, trainingY, testingX, testingY)
	# where X are the features and Y are the labels.
	features = sys.argv[2]
	with open(features) as infile:
		feature_reader = csv.reader(infile)
		num_rows = sum(1 for row in feature_reader) -1 # -1 for column headers
		infile.seek(0) # return to top of file
		#print(num_rows)
		trainingX = []
		trainingY = []
		testingX = []
		testingY = []
		next(feature_reader) # get rid of column headers
		
		# training features and labels
		for i in range(numLines):
			row = next(feature_reader)
			feats = row[1:-1] # skip dns query name (first col)
			int_feats = []
			for feat in feats:
				int_feats.append(int(feat))
			trainingX.append(int_feats) # features
			trainingY.append(int(row[-1])) # labels
		
		# testing features and labels
		for i in range(num_rows - numLines):
			row = next(feature_reader)
			feats = row[1:-1] # skip dns query name (first col)
			int_feats = []
			for feat in feats:
				int_feats.append(int(feat))
			testingX.append(int_feats) # features
			testingY.append(int(row[-1])) # labels

		#print(trainingX)
		#print(trainingY)
		#print(testingX)
		#print(testingY)

	return (trainingX, trainingY, testingX, testingY)


# ======================================================================================


def main():
	if badArgs(3):
		displayUsage()
		return

	k = sys.argv[1]
	(trainingX, trainingY, testingX, testingY) = splitData(500) # first 500 rows are training data, next ~200 are testing, can alter later
	neigh = KNeighborsClassifier(n_neighbors=k) # create classifier with n_neighbors = k
	neigh.fit(trainingX, trainingY) # fit training features to training labels
	print(neigh.score(testingX, testingY)) # see how well it did



if __name__ == '__main__':
	main()