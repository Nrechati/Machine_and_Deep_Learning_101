# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    LinearRegression.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 15:07:33 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 15:14:33 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from ProgressBar import ft_progress

class LinearRegression() :
	def __init__(self, theta):
		self.theta = np.array(theta)

	def predict_(self, X):
		if self.theta.shape[0] is not X.shape[1] + 1:
			print('Incompatible dimension match between X and theta.')
			return None
		hypothesis = np.ones((X.shape[0], self.theta.shape[0]))
		hypothesis[:,1:] = X
		return hypothesis.dot(self.theta)

	def vec_gradient(self, x, y):
		if len(x) is 0 or len(y) is 0 or len(self.theta) is 0\
		or x.shape[1] is not self.theta.shape[0] or x.shape[0] is not y.shape[0]:
			return None
		return (np.transpose(x).dot(x.dot(self.theta).astype(float) - y)) / x.shape[0]

	def cost_elem_ (self, X, Y) :
		prediction = self.predict_(X)
		if prediction is None or prediction.shape != Y.shape :
			print ("Error in prediction or prediction's shape")
			return None
		return (0.5 / X.shape[0]) * (prediction - Y)**2

	def cost_(self, X, Y):
		cost_elements = self.cost_elem_(X, Y)
		return np.sum(cost_elements)

	def fit_(self, X, Y, alpha, n_cycle):
		hypothesis = np.ones((X.shape[0], self.theta.shape[0]))
		hypothesis[:, 1:] = X
		X = hypothesis
		for j in ft_progress(range(n_cycle)):
			self.theta -= alpha * self.vec_gradient(X, Y)
		return self.theta

	def plot_hypothesis_(self, axis, pred, values, xlabel='X values', ylabel='Y values', title='Title'):
		plt.scatter(axis, values)
		plt.plot(axis, pred)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title)
		plt.grid()
		plt.show()

	def scatter_hypothesis_(self, axis, pred, values, xlabel='X values', ylabel='Y values', title='Title', legendloc='upper right'):
		plt.scatter(axis, values, label='Sell price')
		plt.scatter(axis, pred, s=10, label='Predicted sell price')
		plt.legend(loc=legendloc, shadow=True)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title)
		plt.grid()
		plt.show()

	def scatter_3d_(self, x1, x2, y_true, y_pred):
		fig = plt.figure()
		ax = Axes3D(fig)
		ax.scatter(x1, x2, y_true)
		ax.scatter(x1, x2, y_pred)
		plt.show()

	def plot_cost_(self, X, Y):
		saved_theta = self.theta
		theta0_var = np.linspace(80, 100, 6)
		theta1_var = np.linspace(-14, -4, 50)
		cost_result = np.ones(50)
		for i, theta0 in enumerate(theta0_var):
			self.theta[0] = theta0
			for i, theta1 in enumerate(theta1_var):
				self.theta[1] = theta1
				cost_result[i] = self.cost_(X,Y)
			plt.plot(theta1_var, cost_result)
		self.theta = saved_theta
		for i, theta1 in enumerate(theta1_var):
			self.theta[1] = theta1
			cost_result[i] = self.cost_(X, Y)
		plt.plot(theta1_var, cost_result)
		plt.ylim(0, 200)
		plt.grid()
		plt.show()
