from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn import svm
import csv
import sys
import os


def displayUsage():
	string = "\ndemo.py\n"
	string += "---------------------------------------"
	string += "\nComputes information from various model from feature data\n"
	string += "\nInputs: a .csv file of dns query name features\n"
	string += "usage: python demo.py <training.csv>"
	print(string)

def badArgs(numArgsRequired):
	return len(sys.argv) != numArgsRequired


def splitData(numLines, features):
	# splits data into training and testing. 
	# returns tuple of (trainingX, trainingY, testingX, testingY)
	# where X are the features and Y are the labels.
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
	if badArgs(2):
		displayUsage()
		return

	with open(sys.argv[1]) as infile:
		feature_reader = csv.reader(infile)
		num_rows = sum(1 for row in feature_reader) -1 # -1 for column headers
		infile.seek(0) # return to top of file
	(trainingX, trainingY, unused1, unused2) = splitData(num_rows-1, sys.argv[1]) # first 500 rows are training data, next ~200 are testing, can alter later


	print("------------------------------------")
	print("Training a Support Vector Machine...")
	clf = svm.SVC(gamma='scale')
	clf.fit(trainingX, trainingY)

	print("------------------------------------")


	while True:
		try:
			qry_name = input("\nPlease enter a sample DNS query name to be classified:\n")
			#print(qry_name)

				
			if "www." in qry_name:
				qry_name = qry_name.lstrip("www.")
			
			length = len(qry_name)
			numDigits = sum(c.isdigit() for c in qry_name)
			numPeriods = sum(c == '.' for c in qry_name)
			numDashes = sum(c == '-' for c in qry_name)
			includesCom = (1 if ".com" in qry_name else 0)
			includesNet = (1 if ".net" in qry_name else 0)
			includesOrg = (1 if ".org" in qry_name else 0)
			includesEdu = (1 if '.edu' in qry_name else 0)
			includesCdn = (1 if "cdn" in qry_name else 0)
			includesAds = (1 if "ads" in qry_name else 0)

			features = [length, numDigits, numPeriods, numDashes, includesCom, includesNet, includesOrg, includesEdu, includesCdn, includesAds]

			prediction = clf.predict([features])
			if prediction[0] == 0:
				print("secondary")
			else:
				print("primary")

		except KeyboardInterrupt:
			print("\nProgram Exited")
			quit()


if __name__ == '__main__':
	main()