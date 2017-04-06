from __future__ import division, print_function

from datetime import datetime
import re

reftime  = datetime(1995, 7, 1)  
epoch = datetime.utcfromtimestamp(0)
reftsec  = (reftime-epoch).total_seconds() 
monthdict = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep':9, 'Oct':10, 'Nov':11, 'Dec':12}

def replace_some_char(line): 
    return line.replace('[', ' ').replace(']','').replace('"','')  

def faster_straptimpe(stringtime):
    """
    This is hand coded because the datetime.straptime was slow!
    """
    return datetime(
        int(stringtime[8:12]), # Year 
        monthdict[stringtime[4:7]], # Month
        int(stringtime[1:3]), # Day 
        int(stringtime[13:15]), # Hour
        int(stringtime[16:18]), # Minute
        int(stringtime[19:21]) #Second
    )

def convert_time_strtoint(stringtime):
    return int(( faster_straptimpe(stringtime)-reftime).total_seconds())

def convert_time_inttostr(inttime):
    time  = datetime.utcfromtimestamp(inttime+reftsec) 
    return time.strftime('%d/%b/%Y:%H:%M:%S') #

#assert convert_time_inttostr(1)=='01/Jul/1995:00:00:01'

