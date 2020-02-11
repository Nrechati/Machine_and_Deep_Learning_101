# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Question.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 12:54:09 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 12:58:33 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from math_fct import is_numeric

class Question:
    def __init__(self, column, value, features):
        self.column = column
        self.value = value
        self.features = features

    def match(self, example):
        val = example[self.column]
        if is_numeric(val):
            return val >= self.value
        else:
            return val == self.value

    def __repr__(self):
        condition = "=="
        if is_numeric(self.value):
            condition = ">="
        return "Is %s %s %s?" % (
            self.features[self.column], condition, str(self.value))
