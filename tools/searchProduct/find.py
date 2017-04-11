#!/usr/bin/env python

import _multiprocessing
import count,sys,re,time
# sys.path.append("/Users/user/Documents/project/PycharmProjects/call_ds/call_sa.py")
from sa import *


def RunOne(file):
    file = open(file,'r')
    hotel = file.readline()
    print time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime())
    while hotel !='':
        #print "the current hotel is :",hotel
        count.start(int(hotel))
        hotel = file.readline()
    print time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime())

def Multi_Run(fun,data,num):
    pool = _multiprocessing.pool(num)
    pool.apply_async(fun,data)
    pool.close()
    pool.join()


def runMany(file):
    file = open(file,'r')
    hotels = []
    while 1:
        lines = file.readlines(1000)
        if not lines:
            for line in lines:
                hotels.append((line,1,2))
            Multi_Run(process,hotels)
        else:
            break



if __name__ =='__main__':
     file = sys.argv[1]
     runMany("hotel_id")
