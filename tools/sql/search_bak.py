#!/usr/bin/python
# -*- coding:utf-8 -*-
import os
from conf import *

###
##
#	连接数据库
##
###

def connect(HOST,PORT,USER,PWD,DB):
    try:
	conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PWD,db=DB,charset='utf-8')
	cursor = conn.cursor()
    except MySQLdb.Error e:
	print "error code %s,error msg %s" %(e.args[0],e.args[1])

###
##
#	连接数据库
##
###

def select(sql):
    try:
	sqlstr = open(sql,'r').read()
	cursor.execute(sql)
    except MySQLdb.Error e:
	print "error code %s,error msg %s" %(e.args[0],e.args[1])

def show(lines):
    for line in lines:
	print line
##	
##	connect()
##
##
def main():
    connect()

if __name__ == '__main__':
    main()
