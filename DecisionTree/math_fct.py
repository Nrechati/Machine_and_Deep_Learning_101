# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math_fct.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 12:55:23 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 13:08:01 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import collections
import numpy as np

from math import log2

def is_numeric(value):
    return isinstance(value, int) or isinstance(value, float)

def entropy(array):
		if type(array) is not np.ndarray or array.size is 0:
			return None
		N = array.shape[0]
		counter = collections.Counter(array)
		counter = np.array(list(counter.items()))
		pi = (counter[:,1].astype(int)) / N
		for i in range(pi.shape[0]):
			pi[i] = pi[i]*log2(pi[i])
		pi_sum = pi.sum()
		return (pi_sum if pi_sum == 0 else -pi_sum)

def gini(array):
	if type(array) is not np.ndarray or array.size is 0:
		return None
	N = array.shape[0]
	counter = collections.Counter(array)
	counter = np.array(list(counter.items()))
	pi = (counter[:,1].astype(int)) / N
	pi = pi ** 2
	pi_sum = pi.sum()
	return (1 - pi_sum)

def information_gain(array_source, array_children_list, criterion):
	if type(array_source) is not np.ndarray\
		or array_source.size is 0\
		or type(array_children_list) is not list\
		or type(array_children_list[0]) is not np.ndarray:
		return None
	if criterion is not 'gini' and criterion is not 'entropy':
		return None
	func = entropy if criterion is 'entropy' else gini
	N = array_source.shape[0]
	ni_N_Si = [(len(child) / N) * func(child) for child in array_children_list]
	return(func(array_source) - sum(ni_N_Si))
