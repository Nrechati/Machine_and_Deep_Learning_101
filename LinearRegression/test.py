# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/11 15:07:37 by nrechati          #+#    #+#              #
#    Updated: 2020/02/11 15:19:02 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import pandas as pd
import numpy as np

from colorama import Fore, Style
from sklearn.metrics import mean_squared_error
from LinearRegression import LinearRegression

#Get the data
data = pd.read_csv("./Dataset/spacecraft_data.csv")

#X-values for Single variable linear regression
XAge = np.array(data['Age']).reshape(-1,1)
XThrust = np.array(data['Thrust_power']).reshape(-1, 1)
XTmeters = np.array(data['Terameters']).reshape(-1, 1)

#X-values for Multiple variables linear regression
Xall = np.ones((XAge.shape[0], 2))
Xall = np.concatenate((XAge, XThrust, XTmeters), axis=1)

#Y-values data feeded to the model
YSell_Price = np.array(data['Sell_price']).reshape(-1, 1)

#############################################################
##    SINGLE VARIABLE LINEAR REGRESSION GRADIENT DESCENT   ##
#############################################################
print(f'{Fore.GREEN}╔═╗┬┌┐┌┌─┐┬  ┌─┐  ╦  ╦┌─┐┬─┐┬┌─┐┌┐ ┬  ┌─┐  ╦  ╔═╗╔╦╗')
print(f'{Fore.GREEN}╚═╗│││││ ┬│  ├┤   ╚╗╔╝├─┤├┬┘│├─┤├┴┐│  ├┤   ║  ║ ╦ ║║')
print(f'{Fore.GREEN}╚═╝┴┘└┘└─┘┴─┘└─┘   ╚╝ ┴ ┴┴└─┴┴ ┴└─┘┴─┘└─┘  ╩═╝╚═╝═╩╝\n')

#	Linear Gradient Descent Age/Sell Price
LGD_age = LinearRegression(np.array([[1.], [1.]]))
print(f'{Fore.MAGENTA}Fitting on age data')
LGD_age.fit_(XAge, YSell_Price, alpha=1.6e-4, n_cycle=20000)
YHypothesis = LGD_age.predict_(XAge)
print(f'{Fore.GREEN}Mean Squared Error = {Fore.YELLOW}{mean_squared_error(YSell_Price, YHypothesis)}')
LGD_age.scatter_hypothesis_(XAge, YHypothesis, YSell_Price, xlabel='x: Age (in years)', ylabel='y: Sell price (in k$)', title='Single LGD on Age')

#	Linear Gradient Descent Thrust/Sell Price
LGD_thrust = LinearRegression(np.array([[1.], [1.]]))
print(f'{Fore.MAGENTA}Fitting on thrust data')
LGD_thrust.fit_(XThrust, YSell_Price, alpha=1.5e-5, n_cycle=20000)
YHypothesis = LGD_thrust.predict_(XThrust)
print(f'{Fore.GREEN}Mean Squared Error = {Fore.YELLOW}{mean_squared_error(YSell_Price, YHypothesis)}')
LGD_thrust.scatter_hypothesis_(XThrust, YHypothesis, YSell_Price, xlabel='x: Age (in years)', ylabel='y: Sell price (in k$)', title='Single LGD on Thrust')

#	Linear Gradient Descent Tmeters/Sell Price
LGD_Tmeters = LinearRegression(np.array([[1.], [1.]]))
print(f'{Fore.MAGENTA}Fitting on Tmeters data')
LGD_Tmeters.fit_(XTmeters, YSell_Price, alpha=1.6e-4, n_cycle=20000)
YHypothesis = LGD_Tmeters.predict_(XTmeters)
print(f'{Fore.GREEN}Mean Squared Error = {Fore.YELLOW}{mean_squared_error(YSell_Price, YHypothesis)}')
LGD_Tmeters.scatter_hypothesis_(XTmeters, YHypothesis, YSell_Price, xlabel='x: Age (in years)', ylabel='y: Sell price (in k$)', title='Single LGD on Terameters')

print('\n##################################################\n')
#############################################################
##    MULTIPLE VARIABLE LINEAR REGRESSION GRADIENT DESCENT   ##
#############################################################
print(f'{Fore.GREEN}╔╦╗┬ ┬┬ ┌┬┐┬┌─┐┬  ┌─┐  ╦  ╦┌─┐┬─┐┬┌─┐┌┐ ┬  ┌─┐┌─┐  ╦  ╔═╗╔╦╗')
print(f'{Fore.GREEN}║║║│ ││  │ │├─┘│  ├┤   ╚╗╔╝├─┤├┬┘│├─┤├┴┐│  ├┤ └─┐  ║  ║ ╦ ║║')
print(f'{Fore.GREEN}╩ ╩└─┘┴─┘┴ ┴┴  ┴─┘└─┘   ╚╝ ┴ ┴┴└─┴┴ ┴└─┘┴─┘└─┘└─┘  ╩═╝╚═╝═╩╝\n')

#	Multi-Linear Gradient Descent for  Age/Sell_Price
MLGD = LinearRegression(np.array([[1.], [1.], [1.], [1.]]))
print(f'{Fore.MAGENTA}Fitting on multi variable data')
MLGD.fit_(Xall, YSell_Price, alpha=0.98e-4, n_cycle=500000)
print(f'{Fore.CYAN}Final theta is :\n {Fore.YELLOW}{MLGD.theta}')
print(f'{Fore.MAGENTA}Prediction')
YHypothesis = MLGD.predict_(Xall)
print(f'{Fore.GREEN}Mean Squared Error = {Fore.YELLOW}{mean_squared_error(YSell_Price, YHypothesis)}{Style.RESET_ALL}')
MLGD.scatter_hypothesis_(XAge, YHypothesis, YSell_Price, xlabel='x: Age (in years)', ylabel='y: Sell price (in k$)', title='Multi variable LGD Age/Price')

#	Multi-Linear Gradient Descent  / Sell_Price
MLGD = LinearRegression(np.array([[1.], [1.], [1.], [1.]]))
print(f'{Fore.MAGENTA}Fitting on multi variable data')
MLGD.fit_(Xall, YSell_Price, alpha=0.98e-4, n_cycle=500000)
print(f'{Fore.CYAN}Final theta is :\n {Fore.YELLOW}{MLGD.theta}')
print(f'{Fore.MAGENTA}Prediction')
YHypothesis = MLGD.predict_(Xall)
print(f'{Fore.GREEN}Mean Squared Error = {Fore.YELLOW}{mean_squared_error(YSell_Price, YHypothesis)}{Style.RESET_ALL}')
MLGD.scatter_hypothesis_(XThrust, YHypothesis, YSell_Price, xlabel='x: Thrust (in 10Km/s)', ylabel='y: Sell price (in k$)', title='Multi variable LGD Thrust/Price', legendloc='upper left')

#	Multi-Linear Gradient Descent  / Sell_Price
MLGD = LinearRegression(np.array([[1.], [1.], [1.], [1.]]))
print(f'{Fore.MAGENTA}Fitting on multi variable data')
MLGD.fit_(Xall, YSell_Price, alpha=0.98e-4, n_cycle=500000)
print(f'{Fore.CYAN}Final theta is :\n {Fore.YELLOW}{MLGD.theta}')
print(f'{Fore.MAGENTA}Prediction')
YHypothesis = MLGD.predict_(Xall)
print(f'{Fore.GREEN}Mean Squared Error = {Fore.YELLOW}{mean_squared_error(YSell_Price, YHypothesis)}{Style.RESET_ALL}')
MLGD.scatter_hypothesis_(XTmeters, YHypothesis, YSell_Price, xlabel='x: Distance totalizer value of spacecraft (in Terameters)', ylabel='y: Sell price (in k$)', title='Multi variable LGD Tmeters/Price', legendloc='upper right')
