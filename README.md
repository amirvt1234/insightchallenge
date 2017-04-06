# Inisght Data Engineering Challenge

## Summary

### Note1: Upadted version: The previous code was not writing the values that ver equal to the kth most active users while they will be still considered among the top k active users. The new version accounts for those users/requests which can be relevent for features 1 and 2. However it also add O(N) to time complexity. This can be further modified for better performance.  

### Note2: Upadted version: The previous version was using the np.argpartition to find the k largest busy periods which was not stable sorting. This was resulting in wrong answers. In this version I have replaced it with a simple algorithim. However the time complexity of this method is O(kN)  

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







