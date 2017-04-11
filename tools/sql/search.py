#!/usr/bin/python
# -*-  coding:utf-8  -*-
import MySQLdb,pymssql
import sys,re
import os
from conf import * 

print BASE_PATH
sql = BASE_PATH+'/sql'
print sql

    #############################
    #	    连接数据库		#
    #############################

def connect(HOST,PORT,USER,PWD,DB):
    try:
	global conn
	global cursor
#	conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PWD,db=DB,charset='utf-8')
	conn = MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PWD,db=DB)
	cursor = conn.cursor()
	print "连接数据库成功"
    except MySQLdb.Error, e:
	print "error code %s,error msg %s" %(e.args[0],e.args[1])
    
    #############################
    #	    连接sqlserver   	#
    #############################
def SqlServer(HOST,PORT,USER,PWD,DB):
    try:
	global s_conn
	global s_cursor
	s_conn = pymssql.connect(host=HOST,user=USER,password=PWD,database=DB,port=PORT)
	s_cursor = conn.cursor()
	print "连接sqlserver成功"
    except pymssql.Error,e:
	print "sqlserver 连接错误码%s,错误信息：%s"%(e.args[0],e.args[1])


    #############################
    #		select		#
    #############################

def select(sql):
    try:
	file = open(sql,'r')
	title = file.readline()
	sqlstr = file.read()
	cursor.execute(sqlstr)

	print title
	lines = cursor.fetchall()
	show(lines)
    except MySQLdb.Error, e:
	print "error code %s,error msg %s" %(e.args[0],e.args[1])

    #############################
    #	    update		#
    #############################
#def update(updt):
#    try:
#	file = open(update,'r')

sqlFile =BASE_PATH+'/PromotionProduct_u.sql'
print "sqlFile is :",sqlFile
def readPromotionProdcut(source):
    a = []
    for line in open(source,'r'):
#	promId = line.split("\t")[0]
#	hotelId = line.split("\t")[1]
#	roomId = line.split("\t")[2]
#	rpId = line.split("\t")[3]
#	coupon = line.split("\t")[4]
#	start = line.split("\t")[5]
#	end = line.split('\t')[6]
#	line = line.split('\n')
#	print line


	ls = re.split('[\t\n]',line)
	b = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6])  
	a.append(b)
	print a
	'''
	for j in range(0,7):
#	    ls = line.split('/t')
	    ls =re.split('[\t\n]',line)
	    b = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6])
	    print b
	a.append(b)
	print a
    strSql = open(sqlFile,'r')
    print "host= %s ,port = %s,user=%s,password = %s,db=%s"%(PRO_HOST,PRO_PORT,PRO_USER,PRO_PASSWORD,PRO_DBNAME)
    SqlServer(PRO_HOST,PRO_PORT,PRO_USER,PRO_PASSWORD,PRO_DBNAME)
'''
#    connect(PRO_HOST,PRO_PORT,PRO_USER,PRO_PASSWORD,PRO_DBNAME) 
#    cursor = conn.cursor()
   # cursor.excutemany(strSql,a)
#	print "promoId :",promId
#	print "hotelId  ",hotelId
#	print "roomId : ",roomId
#	print "rpId： ",rpId
#	print "coupon: ",coupon
#	print "start:",start
#	print "end: ",end
    

#def insert(type,source):
#    try:
#	if type == 1:
#	    file = open(source,'r')
#	    for line in file.readline:
#		promId = line[0]
#		hotelId = line[1]
#		roomId = line[2]
#		rpId = line[3]
#		coupon = line[4]
#		start = line[5]
#		end = line[6]
#		print "promoId,"
#        strSql = open(ProProductInc,'w')
#
#	file = open(insert,'r')
#	for line in file.readline():
#	    con.excute()

    #############################
    #	    show_result		#
    #############################

def show(lines):
    for line in lines:
	print line

def main():
    ## 没有入参
    print "\033[31m	1.查询	    1.1sql	    \033[0m"
    print "\033[31m	2.插入 2.1 promotionproduct全量\    2.2 promotionproduct增量	\033[0m"
    print "\033[31m	3.更新	3.1 更新promotion_product增量时间   3.2 更行promotion_product 数据	\033[0m"
    print "\033[31m	4.删除	4.1 删除rp流水表中超前的数据    \033[0m"
    connect(HOST,PORT,USER,PWD,DB)
    select(sql)
#    show()

conn = 0


if __name__ == '__main__':
#    main()
    file = sys.argv[1]
    readPromotionProdcut(file)
