# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Node.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 12:54:28 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 13:08:04 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import matplotlib.pyplot as plt

class Node:
    def __init__(self, question, true_branch, false_branch, data=None):
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

    def scatter_node(self, data):
        plt.scatter(self.true_branch[:,self.question.column], self.true_branch[:,-1], s=10, label='True rows')
        plt.scatter(self.false_branch[:,self.question.column], self.false_branch[:,-1], s=10, label='False rows')
        plt.legend(loc='upper left', shadow=True)
        plt.xlabel('F' + self.question.column)
        plt.ylabel('Class labels values')
        plt.title('Distribution of data after node')
        plt.grid()
        plt.show()
