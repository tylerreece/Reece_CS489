from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import tree
from sklearn import svm
import csv
import sys
import os


def displayUsage():
	string = "\nclassification.py\n"
	string += "---------------------------------------"
	string += "\nComputes information from various model from feature data\n"
	string += "\nInputs: a .csv file of dns query name features\n"
	string += "usage: python classification.py <input.csv>"
	print(string)

def badArgs(numArgsRequired):
	return len(sys.argv) != numArgsRequired


def splitData(numLines):
	# splits data into training and testing. 
	# returns tuple of (trainingX, trainingY, testingX, testingY)
	# where X are the features and Y are the labels.
	features = sys.argv[1]
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

	(trainingX, trainingY, testingX, testingY) = splitData(600) # first 500 rows are training data, next ~200 are testing, can alter later
	print("\nTesting using K-Nearest-Neighbors with various sizes of K (1-30)...")
	print("i\t|\t% Accuracy")
	print('------------------------------------')
	for i in range(1,31):
		neigh = KNeighborsClassifier(n_neighbors=i)
		neigh.fit(trainingX, trainingY)
		print("i: " + str(i) + "\t|\t" + str(neigh.score(testingX, testingY)))

	print("------------------------------------")
	print("\nTesting using Multi-layer Perceptron using back propagation...")
	clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(10,2), random_state=1)
	clf.fit(trainingX, trainingY)
	print("score: " + str(clf.score(testingX, testingY)) + "\n")
	
	print("------------------------------------")
	print("\nTesting using a Decision Tree Classifier...")
	clf = tree.DecisionTreeClassifier()
	clf.fit(trainingX, trainingY)
	print("score: " + str(clf.score(testingX, testingY)))

	print("------------------------------------")
	print("\nTesting using a Support Vector Machine...")
	clf = svm.SVC(gamma='scale')
	clf.fit(trainingX, trainingY)
	print("score: " + str(clf.score(testingX, testingY)))

	print("------------------------------------")


if __name__ == '__main__':
	main()