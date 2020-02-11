# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 14:19:47 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 14:29:03 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np

from colorama import Fore, Style
from LogisticRegression import LogisticRegression
from math_fct import accuracy, recall, precision, f1_score

def main():
	df_train = pd.read_csv('./dataset/train_dataset_clean.csv', delimiter=',', header=None, index_col=False)
	x_train, y_train = np.array(df_train.iloc[:, 1:82]), np.array(df_train.iloc[:, 0])
	y_train.shape = [y_train.shape[0], 1]
	df_test = pd.read_csv('./dataset/test_dataset_clean.csv', delimiter=',', header=None, index_col=False)
	x_test, y_test = np.array(df_test.iloc[:, 1:82]), np.array(df_test.iloc[:, 0])
	y_test.shape = [y_test.shape[0], 1]

	# We set our model with our hyperparameters : alpha, max_iter, verbose and learning_rate
	Model = LogisticRegression(alpha=0.01, max_iter=500, verbose=True, learning_rate='constant')
	# We fit our Model to our dataset and display the score for the train and stest datasets
	Model.fit(x_train, y_train)
	print(f'{Fore.CYAN}Score on train dataset : {Model.score(x_train, y_train)}')
	y_pred = Model.predict(x_test)
	print(f'{Fore.CYAN}Score on test dataset : {(y_pred == y_test).mean()}{Style.RESET_ALL}')
	print(f'{Fore.MAGENTA}Accuracy : {accuracy(y_test, y_pred)}')
	print(f'{Fore.MAGENTA}Precision : {precision(y_test, y_pred)}')
	print(f'{Fore.MAGENTA}Recall : {recall(y_test, y_pred)}')
	print(f'{Fore.MAGENTA}F1_Score : {f1_score(y_test, y_pred)}')
	Model.plot_loss()

if __name__ == "__main__":
	main()
