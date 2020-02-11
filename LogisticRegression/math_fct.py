# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    math_fct.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 14:19:39 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 14:31:45 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def accuracy(y_true, y_pred):
	success = 0.
	sample = y_true.shape[0]
	for i in range(sample):
		if y_true[i] == y_pred[i]:
			success += 1
	return(success/sample)

def recall(y_true, y_pred, pos_label=1):
	label_match = 0
	sucess = 0
	for i in range(y_true.shape[0]):
		if y_true[i] == pos_label:
			label_match += 1
			if y_pred[i] == y_true[i]:
				sucess += 1
	return(sucess/label_match)

def precision(y_true, y_pred, pos_label=1):
	label_match = 0
	sucess = 0
	for i in range(y_true.shape[0]):
		if y_pred[i] == pos_label:
			label_match += 1
			if y_pred[i] == y_true[i]:
				sucess += 1
	return(sucess/label_match)

def f1_score(y_true, y_pred, pos_label=1):
	P = precision(y_true, y_pred, pos_label)
	R = recall(y_true, y_pred, pos_label)
	return (2 * ((P * R) / (P + R)))
