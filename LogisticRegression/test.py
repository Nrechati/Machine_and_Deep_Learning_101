# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 14:19:47 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 14:47:34 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np

from colorama import Fore, Style
from LogisticRegression import LogisticRegression
from math_fct import accuracy, recall, precision, f1_score

def main():
	#Get the train dataset
	print(f'{Fore.CYAN}Getting the train dataset', end="")
	df_train = pd.read_csv('./Dataset/train_dataset_clean.csv', delimiter=',', header=None, index_col=False)
	x_train, y_train = np.array(df_train.iloc[:, 1:82]), np.array(df_train.iloc[:, 0])
	y_train.shape = [y_train.shape[0], 1]
	print(f'\t✔ Ok')

	#Get the test dataset
	print(f'{Fore.CYAN}Getting the test dataset', end="")
	df_test = pd.read_csv('./Dataset/test_dataset_clean.csv', delimiter=',', header=None, index_col=False)
	x_test, y_test = np.array(df_test.iloc[:, 1:82]), np.array(df_test.iloc[:, 0])
	y_test.shape = [y_test.shape[0], 1]
	print(f'\t✔ Ok')

	# Initialize the model
	print(f'{Fore.YELLOW}Model Initialization', end="")
	Model = LogisticRegression(alpha=0.1, max_iter=2000, verbose=True, learning_rate='constant')
	print(f'\t\t✔ Ok')

	# Training the model
	print(f'{Fore.MAGENTA}Training the model')
	Model.fit(x_train, y_train)

	#Testing the model
	print(f'{Fore.CYAN}Score on train dataset : {Model.score(x_train, y_train)}')
	y_pred = Model.predict(x_test)
	print(f'{Fore.CYAN}Score on test dataset : {(y_pred == y_test).mean()}{Style.RESET_ALL}')
	print(f'{Fore.MAGENTA}Accuracy : {accuracy(y_test, y_pred)}')
	print(f'{Fore.MAGENTA}Precision : {precision(y_test, y_pred)}')
	print(f'{Fore.MAGENTA}Recall : {recall(y_test, y_pred)}')
	print(f'{Fore.MAGENTA}F1_Score : {f1_score(y_test, y_pred)}{Style.RESET_ALL}')
	Model.plot_loss()

if __name__ == "__main__":
	main()
