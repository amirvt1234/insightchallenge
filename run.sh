#!/usr/bin/env bash

#echo -e '##############################################################'
#echo '                            TASK 1                   '
#echo -e '##############################################################'

#python3 src/read_input.py log_input/log.txt
python src/process_log.py log_input/log.txt log_output/hosts.txt log_output/resources.txt log_output/hours.txt log_output/blocked.txt   

