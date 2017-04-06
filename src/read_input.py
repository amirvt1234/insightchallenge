from __future__ import division, print_function

import itertools
import sys
import csv
import io

import utils

def main(argv):
    if len(argv) < 1 :
        print ('No input file provided')
        sys.exit(2)
    try:
        log_file = open(sys.argv[1], "r",encoding = "ISO-8859-1")
    except:
        log_file = open(sys.argv[1], "r")
    start_time = time.time()
    data = read_from_file(log_file) 

def read_from_file(log_file, n_start=0, n_end=None):
    """
    Reads chunks of data 
    """
    times_pool, users_pool, requests_pool, bytes_pool, replies_pool  = [], [], [], [], [] 
    reader = csv.reader(itertools.islice(log_file, n_start, n_end), delimiter=' ', quotechar='"')
    for line in reader:
        users_pool.append(line[0])
        times_pool.append(line[3])
        req = line[5].split()
        if len(req)<2: req.append(req[0])
        requests_pool.append(req)
        replies_pool.append(int(line[-2]))
        bytes_pool.append(int(line[-1].replace('-','0')))
        assert line[4] == '-0400]' # A sanity test
    return (users_pool, times_pool, requests_pool, replies_pool, bytes_pool)

if __name__ == '__main__':
	main(sys.argv[1:])
	sys.exit(0)

