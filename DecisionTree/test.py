# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 12:53:35 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 13:31:34 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np

from colorama import Fore, Style
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from DecisionTreeClassifier import DecisionTreeClassifier

def main():
	# Get iris dataset
	iris = load_iris()
	X = pd.DataFrame(iris.data)
	y = pd.DataFrame(iris.target)
	# Split Train/Test set
	X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7, random_state=1)

	# Setup train dataset
	X_train = X_train.values
	y_train = y_train.values
	train_data = np.concatenate((X_train, y_train), axis=1)

	# Setup test dataset
	X_test = X_test.values
	y_test = y_test.values
	test_data = np.concatenate((X_test, y_test), axis=1)

	#Data set parameters
	features = ["sepal_L", "sepal_W", "petal_L", "petal_W"]
	labels = ["Setosa\t", "Versicolour", "Virginica"]

	#Create Decision trees
	MyTree = DecisionTreeClassifier(features, labels)
	MyTree.root = MyTree.fit(train_data)

	#Print the tree
	MyTree.print_tree(MyTree.root)

	#Predict test set
	for row in test_data:
		prediction = MyTree.classify(row, MyTree.root)
		print (f"{Fore.YELLOW}Actual: %s\t{Fore.GREEN}Predicted: %s{Style.RESET_ALL}" % (labels[int(row[-1])], prediction))

if __name__ == "__main__":
	main()
