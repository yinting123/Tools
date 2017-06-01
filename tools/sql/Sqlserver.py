#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import re

import pymssql
from  conf.MsqConf import *

#reload(sys)
#sys.setdefaultcoding('utf8')

class SqlServerDB:
    host = ''
    port = 0
    user = ''
    pwd = ''
    db = ''
    
    def __init__(self,host,port,user,password,dbname):
        self.host = host
        self.port = port
        self.user = user
        self.pwd = password
        self.db = dbname

    def __GetConnect(self):
        print "host:%s ,port:%s,user:%s,password:%s,dbname=%s"%(self.host,self.port,self.user,self.pwd,self.db)
        if (not self.host) or (not self.port) or (not self.user) or (not self.pwd) or (not self.db):
            print ("请正确设置数据库的连接信息")
        self.conn = pymssql.connect(host = self.host,port = self.port ,user = self.user,password = self.pwd,database = self.db,charset = 'utf8')
        if not self.conn:
            print "连接数据库失败"
        else :
            cursor = self.conn.cursor()
            print "连接成功"
            return cursor
	    
    def getValues(self,DataSource):
        values = []
        lines = open(DataSource,'r')
        print "lines is :",lines
        for line in lines:
            print "line = ",line
            ls = re.split('\\s | ## | \r | \n',line)
            #tmp = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5]+' '+ls[6],ls[7]+' '+ls[8])
            tmp = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6],ls[7])
            values.append(tmp)
            print "tmp is:",tmp
            del tmp
            print values
        return values


    def insert(self,sql,data):
        '''
            批量插入的sql语句中不能使用use db XXX
        '''
        cursor = self.__GetConnect()
        sqlStr = open(sql,'r').read()
        print "sqlString is :\n",sqlStr
        values = self.getValues(data)
        print "values in insert is :",values 
        affected = cursor.executemany(sqlStr,values)
        print "affected lines is :",affected
        self.conn.commit()
        cursor.close()
        self.conn.close()


    def select(self,SqlFile):
        sql = open(SqlFile,'r').read()
        print "sqlString is :%s"%sql
        cursor = self.__GetConnect()
        cursor.execute(sql)
        lines = cursor.fetchall()
        for line in lines:
            # print str(line).encode('utf-8')
            print line
        cursor.close()
        self.conn.close()
    
    def update(self,SqlFile):
        SqlStr = open(SqlFile,'r').read()
        print "sqlStr is :\n",SqlStr
        cursor = self.__GetConnect()
        cursor.execute(SqlStr)
        self.conn.commit()
        cursor.close()
        self.conn.close()

if __name__ == '__main__':
    len = len(sys.argv)
    print "len is ", len
    try:
        if 2 == len:
            SqlServer =  SqlServerDB(pro_host,pro_port,pro_user,pro_password,pro_dbname)
            SqlServer =  SqlServerDB(phost,pport,puser,ppassword,pdbname)
            # SqlServer.getValues(sys.argv[1])
            SqlServer.select(sys.argv[1])

        if 4 == len:
            #SqlServer = SqlServerDB(HOST,PORT,USER,PASSWORD,DBNAME)
            # 76.13库
            # SqlServer = SqlServerDB(s_host,s_port,s_user,s_password,s_dbname)
            # 促销库
            SqlServer =  SqlServerDB(pro_host,pro_port,pro_user,pro_password,pro_dbname)

            type = int(sys.argv[1])
            SqlFile = sys.argv[2]
            SourceData = sys.argv[3]
            SqlServer.insert(SqlFile,SourceData)
            print "host:%s,port :%s,user: %s , password: %s, dbname: %s"%(HOST,PORT,USER,PASSWORD,DBNAME)
        elif 3 == len:
            #SqlServer = SqlServerDB(HOST,PORT,USER,PASSWORD,DBNAME)
            SqlServer = SqlServerDB(s_host,s_port,s_user,s_password,s_dbname)
            SqlServer =  SqlServerDB(pro_host,pro_port,pro_user,pro_password,pro_dbname)
            #SqlServer =  SqlServerDB(pro_host,pro_port,pro_user,pro_password,pro_dbname)
            type = int(sys.argv[1])
            SqlFile = sys.argv[2]
            if 1 == type:
                SqlServer.select(SqlFile)
            if 2 == type:
                SqlServer.update(SqlFile)
        
        else:
            raise IndexError

    except IndexError:
        #print "\033[35m *************   \t 1.查询\033[0m"
        #print "\033[35m *************   \t 2.更新\033[0m"
        #print "\033[35m *************   \t 3.插入\033[0m"
        #print "\033[35m *************   \t 参数3:要插入的数据\033[0m"
        print "\033[35m \t ./Sqlserver.py 3 sqlFile data \033[0m "
        print "\033[35m \t *********** 参数1：查询方式，1—查询 2—更新 3—插入 \033[0m"
        print "\033[35m	 *********** 参数2：sql语句  参数3：插入数据 \033[0m"
