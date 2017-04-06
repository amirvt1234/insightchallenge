# Inisght Data Engineering Challenge

## Summary

### Note: For feature 3 I have used the numpy argpartition for selecting the k largest elements which is not an stable sorting scheme. Initially I missed the importance of stable soting for this case. I started the project really late. Since I had another deadline but I am aware of the bug. I would appreciate if I be given an extension to fix this bug. But I am fully aware of it and just had no time to fix it. 

This program loads a log text file and performs the following using the data:

- Lists the kth most active host/IP addresses
- Lists the top k requests that consume the most bandwidth
- Lists the 10 busiest k-minutes periods
- Detects the pattern of recent faild login attampts

In order to make the code scalable for larger data sets, this program reads smaller chuncks of data at a time, e.g. default is 100,0000 lines of the file, until it reaches the end. 
It processes the loaded data in memory and stores the necessary information for finding answer to the Features, then loads the next chunk of data. Thus the scalablity of the program does not depend on the file size but it does depend on the number of the users and number of the requests since it stores these information for all data to find the maximum. 

## Dependencies 

- Tested with Python 2.7 (2.7.6) and Python 3.4 (3.4.3)
- It requires NumPy version 1.8.0 or newer for Feature 3; I have tested it with NumPy version 1.11.0

## How can I use it?

The esiest way:

	./run.sh

or

	python src/process_log.py log_input/log.txt log_output/hosts.txt log_output/resources.txt log_output/hours.txt log_output/blocked.txt  

### Note on the performance

Python 3 was faster in loading the data. Performance gain of 20% observed using Python 3







