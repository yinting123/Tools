#!/usr/bin/env python
# -*-coding:utf8 -*-

import  sys
sys.path.append("./")
sys.path.append("./dataFile/")

def readLogFile(file,file2):
    f = open(file,'r')
    fp = open(file2,"w+")

    for line in f.readlines():
        line6 = line.split("\t")
        fp.write(line6[9]+"\n")
        # print line6[9],"\n\n\n"
    fp.close()
    f.close()

if __name__ == "__main__":
    filePath = "/Users/user/Documents/project/PycharmProjects/call_ds/utils/tt"
    readLogFile(filePath)
