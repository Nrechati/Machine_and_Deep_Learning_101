# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ProgressBar.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 10:03:28 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 15:09:49 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os
import time
import sys

color_set = {
    'red': '\033[1;31m',
  		'green': '\033[1;32m',
  		'yellow': '\033[1;33m',
  		'purple': '\033[1;35m',
  		'cyan': '\033[1;36m',
  		'nc': '\033[1;0m',
}

def colored(color):
	try:
		print(color_set[color], end="")
	except KeyError:
		print("Error: Color specified is not in our set:", color)

def ft_progress(count, bar_char="█", size=int(100)):
	os.system('tput civis')
	x = 1
	bar = ''
	total = (len(count))
	start = time.time()
	if (len(bar_char) != 1):
		print("Error: Bar_char choose must be of length one")
		sys.exit(1)
	for elem in count:
		pad_percent = ''
		percent = int((x*size)/total)
		bar = bar_char * percent
		pad = " " * (size - percent)
		pad_percent = " " * (3 - len(str(percent)))
		pad_iter = " " * (len(str(total)) - len(str(x)))
		time_delta = time.time() - start
		progress_left = "[" + pad_percent + str(percent) + "%][ " + bar
		progress_right = pad + " ] " + pad_iter + str(x) + "/" + str(total)
		elapsed_time = " | elapsed time " + "{:.2f}".format(time_delta) + "s     "
		colored('green')
		print (progress_left, end="")
		print (progress_right, end="")
		print (elapsed_time, end="\r")
		x += 1
		yield elem
	print("\n...")
	os.system('tput cnorm')
	colored('nc')
