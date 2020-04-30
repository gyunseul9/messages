#!/bin/bash

TIME=`date +"%Y-%m-%d_%H:%M:%S"`

if [ $# -lt 1 ]; then
	echo -e " "
	echo -e " usage: ./run.sh <value>"
	echo -e " e.g: ./run.sh telegram"
	exit 1;
else

	if [ ${1} = "local" ]; then
		DIR="/home/ubuntu/messages/"
	elif [ ${1} = "ubuntu" ]; then
		DIR="/home/ubuntu/messages/"
	else
		exit 1;
	fi

	source ${DIR}bin/activate

	OUTPUT=$(python3 ${DIR}messages.py $1)
	echo -e "\n"$OUTPUT"\n"

fi
