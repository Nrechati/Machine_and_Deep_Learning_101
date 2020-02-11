# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    DecisionTreeClassifier.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 12:53:02 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 13:31:24 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np

from colorama import Fore, Style
from Question import Question
from Leaf import Leaf
from Node import Node
from math_fct import gini, information_gain, entropy

class DecisionTreeClassifier:
	def __init__(self, features, labels, criterion='gini', max_depth=10):
		self.root = None # Root node of the tree
		self.features = features
		self.labels = labels
		self.criterion=criterion
		self.max_depth=max_depth

	def split_over_question(self, data, question):
		true_rows, false_rows = [], []
		for row in data:
			if question.match(row):
				true_rows.append(row)
			else:
				false_rows.append(row)
		true_rows = np.asarray(true_rows)
		false_rows = np.asarray(false_rows)
		return true_rows, false_rows

	def find_best_split(self, data):
		best_gain = 0
		best_question = None
		n_features = data.shape[1]
		for col in range(n_features):
			values = np.unique(data[:, 0])
			for value in np.nditer(values):
				question = Question(col, value.item(0), self.features)
				true_rows, false_rows = self.split_over_question(data, question)
				if len(true_rows) == 0 or len(false_rows) == 0:
					continue
				child_lst = [true_rows[:,-1], false_rows[:,-1]]
				gain = information_gain(data[:,-1], child_lst, self.criterion)
				if gain >= best_gain:
					best_gain, best_question = gain, question
		return best_gain, best_question

	def fit(self, data, depth=0):
		gain, question = self.find_best_split(data)
		if gain == 0 or depth >= self.max_depth:
			return Leaf(data, self.labels)
		true_rows, false_rows = self.split_over_question(data, question)
		true_branch = self.fit(true_rows, depth + 1)
		false_branch = self.fit(false_rows, depth + 1)
		return Node(question, true_branch, false_branch)

	def classify(self, row, node):
		if isinstance(node, Leaf):
			return node.__repr__()
		if node.question.match(row):
			return self.classify(row, node.true_branch)
		else:
			return self.classify(row, node.false_branch)

	def print_tree(self, node, spacing="+"):
		if isinstance(node, Leaf):
			print(spacing + f'{Fore.YELLOW}Predict {node.__repr__()}')
			return
		print (spacing + f'{Fore.CYAN}{str(node.question)}')
		print (spacing + f'{Fore.GREEN}--> True:')
		self.print_tree(node.true_branch, spacing + "  ")
		print (spacing + f'{Fore.RED}--> False:')
		self.print_tree(node.false_branch, spacing + "  ")
