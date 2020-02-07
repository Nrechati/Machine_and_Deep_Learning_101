# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Python3_installer.sh                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nrechati <nrechati@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/07 10:04:53 by nrechati          #+#    #+#              #
#    Updated: 2020/02/07 10:17:02 by nrechati         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/bin/bash

#Colors
LRED='\033[1;31m'
LGREEN='\033[1;32m'
YELLOW='\033[1;33m'
LPURPLE='\033[1;35m'
LCYAN='\033[1;36m'
NC='\033[0m'

#Printing
ROBOT="c[○┬●]כ  "

printf "${LCYAN}\n${NC}"
printf "${LCYAN}    ╔═╗┬ ┬┌┬┐┬ ┬┌─┐┌┐┌  ╦┌┐┌┌─┐┌┬┐┌─┐┬  ┬       \n${NC}"
printf "${LCYAN}    ╠═╝└┬┘ │ ├─┤│ ││││  ║│││└─┐ │ ├─┤│  │       \n${NC}"
printf "${LCYAN}    ╩   ┴  ┴ ┴ ┴└─┘┘└┘  ╩┘└┘└─┘ ┴ ┴ ┴┴─┘┴─┘     \n${NC}"
printf "${LCYAN}\n${NC}"
printf "${LGREEN}${ROBOT}[Start]:\t\t${LCYAN}Welcome to Python Installer\n${NC}"

#Errors and stuff`
ERROR="${LRED}${ROBOT}[ERROR]:\t\t${LRED}"
USAGE="${LCYAN}${ROBOT}[USAGE]:\t\t./installer.sh [install-[binary-to-install]]\n${NC}"
AVAILABLE="${LPURPLE}${ROBOT}[HELP]:\t\tAvailable install list:\n${NC}${LPURPLE}${ROBOT}[HELP]:\t\t-  \"install-python\" : will check and/or install python 3.7\n${NC}"
ALREADY="${YELLOW}${ROBOT}[WARNING]:\t\tPython is already installed, do you want to reinstall it ?\n${NC}"
PROMPT="${YELLOW}${ROBOT}[WARNING]:\t\t[yes|no]> ${NC}"
REMOVE="${LPURPLE}${ROBOT}[RUN]:\t\t\tPython has been removed.\n${NC}"
RUN_INSTALL="${LGREEN}${ROBOT}[RUN]:\t\t\tRunning Python install\n\n"
INSTALLED="${LGREEN}${ROBOT}[RUN]:\t\tPython has been installed.\n${NC}"
INSTALL_PATH="/goinfre/${USER}"
INSTALL_FOLDER="${INSTALL_PATH}/miniconda"
BIN_FOLDER="${INSTALL_FOLDER}/bin"
NEW_PATH="${BIN_FOLDER}:$(echo $PATH)"
INSTALL_SOURCE="./Miniconda3-latest-MacOSX-x86_64.sh"
DO_IT_MSG="${LGREEN}${ROBOT}[RUN]:\t\tTo add newly installed python binary to shell please run:\n${LGREEN}${ROBOT}[RUN]:\t\t${LCYAN}export PATH=\$INSTALL_PATH/miniconda/bin/condabin:\$PATH\n${LGREEN}${ROBOT}[RUN]:\t\t${LCYAN}export PATH=${BIN_FOLDER}:\$PATH"

if [ -z $1 ]
	then
		printf "${ERROR}Please specify bin you want to install prefix with \"install-\"\n${NC}"
		printf "${AVAILABLE}"
else
	if [ $2 ]
		then
			printf "${ERROR}Only one argument allowed\n${NC}"
			printf "${USAGE}"
			printf "${AVAILABLE}"
	else
		if [ $1 != "install-python" ]
			then
				printf "${AVAILABLE}"
		else
			if [ -d ${INSTALL_FOLDER} ]
				then
					printf "${ALREADY}"
					printf "${PROMPT}"
					read answer
					if [ $answer = "yes" ]
						then
							rm -rf ${INSTALL_FOLDER}
							printf "${REMOVE}"
							printf "${RUN_INSTALL}"
							curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
							bash  ${INSTALL_SOURCE} -b -u -p ${INSTALL_FOLDER}
							rm ${INSTALL_SOURCE}
							printf "${INSTALLED}"
							printf "${DO_IT_MSG}"
					else
						printf "exit."
					fi
			else
				printf "${RUN_INSTALL}"
				curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
				bash  ${INSTALL_SOURCE} -b -u -p ${INSTALL_FOLDER}
				rm ${INSTALL_SOURCE}
				printf "${INSTALLED}"
				printf "${DO_IT_MSG}"
			fi
		fi
	fi
fi
