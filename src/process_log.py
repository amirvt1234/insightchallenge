from __future__ import division, print_function

from collections import defaultdict
import heapq
import io
import time
import itertools
import numpy
import sys
import numpy as np

import utils
import read_input

start_time = time.time()

def process(argv):
    """
    Main function: finds the answer to features 1-4
    """
    start_time = time.time()
    if len(argv) != 5 :
        print ('No input or wrong number of inputs file provided')
        sys.exit(2)   
    try:
        # This works with Python 3.4!
        log_file = open(sys.argv[1], "r",encoding = "ISO-8859-1")
    except:
        # This works with Python 2.7!
        log_file = open(sys.argv[1], "r")
    
    start_line, end_line = 0, 10000 # reads 10000 lines of the file at the time
    t_window = 3600 # the time window for Feature 3 in seconds
    k1 = k2 = k3 = 10 # to finde the k largest
    block_s = '' # initiate string for blocked activities
    request_usage = defaultdict(lambda:0) # initiate a dictinoary for usage of request in byte 
    user_access = defaultdict(lambda:0) # initiate dictinoary to track the users who used maximum 
    login_block = defaultdict(lambda:[0,False,0]) # # initiate dictionary to track blocked users
    t_sec_array = [] 
   
    while True:
        users_pool, times_pool, requests_pool, replies_pool, bytes_pool = read_input.read_from_file(log_file, start_line, end_line)
        if not users_pool:
            break       
        for user, t, request, reply, byte  in zip(users_pool, times_pool, requests_pool, replies_pool, bytes_pool):
            # For feature 1: Collect the number of the times each user has accessed the website
            user_access[user] += 1
            # For feature 2: Collect the usage of each requests in bites
            request_usage[request[1]] += byte
            # For feature 3: Convert time from string to integer
            t_sec = utils.convert_time_strtoint(t)
            t_sec_array.append(t_sec) 
            # For feature 4: Collects the blocked activites
            should_block = False
            should_block = user_login_info(login_block[user], t_sec, request[1], reply, should_block)   #, indexb3
            if should_block == True:
                block_s += '{0} - - {1} -0400] "{2}" {3:d} {4:d}'.format(user, t, " ".join(request), reply, byte)+'\n'
    assert t_sec_array[0] == 1
    
    max_user_access = dict_klargest(user_access, k1)
    max_request_use = dict_klargest(request_usage,k2)
    max_visit_h = visited_in_time_window(t_sec_array, t_window, k3)

    with open(sys.argv[2],'w') as f1:
        for w in max_user_access:
            s1 = '{0},{1:d}'.format(w[1],w[0])
            f1.write(s1+'\n')
    with open(sys.argv[3],'w') as f2:
        for w in max_request_use:
            s2 = '{0}'.format(w[1])
            f2.write(s2+'\n')
    with open(sys.argv[4],'w') as f3:
        for w1, w2 in zip(max_visit_h[0],max_visit_h[1]):
            s3 = '{0} -0400,{1:d}'.format(utils.convert_time_inttostr(w1),int(w2))
            f3.write(s3+'\n')
    with open(sys.argv[5],'w') as f4:
        f4.write(block_s)

    f1.close(); f2.close();  f4.close() 
    print ('It took', time.time()-start_time)


def 	dict_klargest(dictin, k):
    """
    Uses the heapq nlarges method the calculate the k largest elements in a dictionary
    The time order of the method is: O(N log(k))
    Parameters
    ----------
    dictin: input dictionary
    k     : integer the number of elements we want to return 
    """
    dict_list = [(value, key) for key,value in dictin.items()]
    return  heapq.nlargest(10,dict_list)

def visited_in_time_window(timeinsec, rolling_window=3600, k3=10):
    """
    Calculates the visits in the given hour
    Parameters
    The time complexity of the k sorting method is O(kN)
    ----------
    rolling_window: window size in seconds
    k3            : is the number of k largest windows
    """
    time_n = np.array(timeinsec, dtype=int)
    time_unique = np.unique(time_n, return_index=True)
    # Create an array with the size equal to the number of the seconds in batchfile 
    # and fill it with the times it has been accessed during each second
    time_freq = np.zeros(time_n[-1]+rolling_window-1, dtype=int)
    for i in range(len(time_unique[0])-1):
        time_freq[time_unique[0][i]-1] = time_unique[1][i+1]-time_unique[1][i]
    time_freq[time_n[-1]-time_n[0]] = len(time_n)-time_unique[1][-1]
    # Calculate the cumulative sum of the time frequency
    cumsum_time = np.cumsum(time_freq,axis=0)
    #visited_tw = np.zeros(time_n[-1]-rolling_window-time_n[0], dtype=int) # check it
    visited_tw = np.zeros(time_n[-1]-time_n[0], dtype=int)
    # Calculate the frequency in the given time window
    visited_tw[0] = cumsum_time[rolling_window-1]
    for i in range(1,len(visited_tw)): # check it
        visited_tw[i] = cumsum_time[i+rolling_window-1]-cumsum_time[i-1]
    Max_index = np.zeros(k3, int)
    Max_val   = np.zeros(k3, int)
    visited_tw_n = visited_tw
    for i in range(k3):
        idx = np.argmax(visited_tw)
        Max_val[i] = visited_tw[idx]
        Max_index[i]=idx; visited_tw[idx]=0
    return (Max_index+time_n[0],Max_val) 

def user_login_info(block_info, t_sec, request, reply, should_block):
    """
    Checks the condition to whether block the user from accessing or not
    """
    if block_info[1] == True: 
        if t_sec - block_info[0] < 5*60:
            should_block = True
        else:
            block_info[2] = 0
            block_info[1] = False
    if request=='/login':
        if reply == 401 and block_info[1] == False:
            if block_info[2] == 0:
                block_info[0] = t_sec
                block_info[2] += 1 
            elif block_info[2] > 0 and t_sec-block_info[0] <20:
                block_info[2] += 1
                if block_info[2] == 3:
                    block_info[1] = True
                    block_info[0] = t_sec
                    block_info[2] = 0
        elif block_info[1] != True or t_sec - block_info[0] > 5*60:
            block_info[2] = 0
            block_info[1] = False
    return should_block

if __name__ == '__main__':
    process(sys.argv[1:])
    sys.exit(0)




    
