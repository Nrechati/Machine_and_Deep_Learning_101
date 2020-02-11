# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Leaf.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 12:54:35 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 13:27:24 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import collections
import numpy as np

class Leaf:
	def __init__(self, data, labels):
		classes = collections.Counter(data[:, -1])
		self.predictions = np.array(list(classes.items()))
		self.labels = labels

	def __repr__(self):
		label_nb = self.predictions.shape[0]
		sample_size = sum(self.predictions[:,-1])
		output = ""
		for i in range(label_nb):
			output = output + str(self.labels[int(self.predictions[i][0])]).strip() + " : "
			output = output + str(int((self.predictions[i][1] / sample_size) * 100)) + "%"
			if (i + 1) is not label_nb :
				output = output + " or "
		return output
