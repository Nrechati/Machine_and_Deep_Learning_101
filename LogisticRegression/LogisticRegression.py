# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    LogisticRegression.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 14:19:35 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 14:37:20 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
import matplotlib.pyplot as plt

from colorama import Fore, Style
from math import log
from ProgressBar import ft_progress

class LogisticRegression:
	def __init__(self, alpha=0.001, max_iter=1000, verbose=False, verbose_int=10, learning_rate='constant'):
		self.alpha = alpha
		self.max_iter = max_iter
		self.verbose = verbose
		self.verbose_int = verbose_int
		self.learning_rate = learning_rate # can be 'constant' or invscaling'
		self.thetas = np.array([[1.], [1.]])
		self.losses= np.zeros(max_iter + 1)

	def sigmoid(self, x):
		if type(x) is np.ndarray:
			return (1/(1 + np.exp(-x)))
		return 1/(1+np.exp(-x))

	def reg_vec_gradient(self,x, y, lambda_):
		tmp_x = np.ones((x.shape[0], self.thetas.shape[0]))  # Check
		tmp_x[:,1:] = x
		x = tmp_x
		result = 0.
		reg_term = lambda_ * self.thetas
		result = (np.transpose(x).dot(self.sigmoid(x.dot(self.thetas)).astype(float) - y) + reg_term) / x.shape[0]
		return result

	def vec_gradient(self, x, y, y_pred):
		tmp_x = np.ones((x.shape[0], self.thetas.shape[0])) #Check
		tmp_x[:,1:] = x
		x = tmp_x
		if type(x[0]) is np.ndarray:
			return (np.transpose(x).dot(y_pred - y)) #Check
		else:
			return ((y_pred - y) * x)

	def vec_loss(self, y, y_pred, m, eps=1e-15):
		if m is 1:
			return (-(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred)))
		elif m > 1:
			return ((-1/m) * (np.transpose(y).dot(np.log(y_pred + eps)) + ((1 - np.transpose(y))).dot(np.log(1 - (y_pred - eps)))))
		else:
			return None

	def predict(self, x):
		tmp_x = np.ones((x.shape[0], self.thetas.shape[0])) #Check
		tmp_x[:,1:] = x
		x = tmp_x
		return ((self.sigmoid(x.dot(self.thetas)) >= 0.5).astype(int))

	def fit(self, x, y):
		self.thetas = np.zeros((x.shape[1] + 1, 1))
		for j in ft_progress(range(self.max_iter + 1)):
			y_pred = self.predict(x)
			if (self.verbose == True):
				self.losses[j] = self.vec_loss(y, y_pred, y.shape[0])
			self.thetas -= self.alpha * self.reg_vec_gradient(x, y, 20)
		if (self.verbose == True):
			for i in range(self.max_iter + 1):
				if (i % (self.max_iter / self.verbose_int) == 0):
					print(f'{Fore.YELLOW}epoch {i} :\tloss : {self.losses[i]}')

	def	score(self, x, y):
		return ((self.predict(x) == y).mean())

	def plot_loss(self, xlabel='X values', ylabel='Y values', title='Losses / epoch (Regularized)', legendloc='upper left'):
		plt.plot(range(self.losses.shape[0]), self.losses)
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.title(title)
		plt.grid()
		plt.show()
