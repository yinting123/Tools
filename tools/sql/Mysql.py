#!/usr/bin/python
#-*- coding:utf-8 -*-

import re

import MySQLdb
# from tools.sql.conf.MsqConf import *
from generateSql import *
from conf.MsqConf import *


class MysqlDB:
    host = ''
    port =''
    user = ''
    password =''
    dbname = ''
    """
    	初始化	
    """
## @desc    初始化ip端口数据库等连接信息
## @para    参数从Mysql.conf配置中读取
## @return  void无返回
    def __init__(self,host,port,user,password,dbname):
	self.host = host
	self.port = port 
	self.user = user
	self.password = password
	self.dbname = dbname


##  @desc   连接数据库
##  @para   无
##  @return 连接的cursor游标
    def GetConnect(self):
	if not self.dbname:
	    print "请重置数据库"
	self.conn = MySQLdb.connect(host=self.host, port=self.port, user= self.user, passwd=self.password, db=self.dbname)
	if not self.conn:
	    print "连接数据库失败"
	else:
	    cursor = self.conn.cursor()
	    return cursor


    def search(self,SqlFile):
	"""
	    查询某个表，按行返回
	"""
	sqlStr = open(SqlFile,'r').read()
	cursor = self.GetConnect()
	cursor.execute(sqlStr)
	results = cursor.fetchall()
	for line in results:
	    print line
	print "查询完毕"
	self.conn.close()
	cursor.close()

    def update(self,SqlFile):
	"""
	    更新数据，一般为更新操作时间或者有效时间
	"""
	print "MysqlDB，进入到update函数"
	cursor = self.GetConnect()
	sqlStr = open(SqlFile,'r').read()
	affected = cursor.execute(sqlStr)
        print "affected in update is :",affected
	self.conn.commit()
	cursor.close()
	self.conn.close()

	
    def getValues(self,DataSource):
        print 'come to value'
        values = []
        lines = open(DataSource,'r').readlines()
        for line in lines:
            print "line: ",line
            #source = line.replace('\\s+','#')
            #print "source data is:",source
            ls = re.split('\\s | ## | \\r | \\n',line)
            #tmp = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6])  
            #tmp = (ls[0],ls[1],ls[2],ls[3],ls[4])  
            #马甲 7位
            # tmp = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6])
            #中央定价 11位
            # tmp = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6],ls[7],ls[8],ls[9],ls[10])
            #马甲7+15位
            tmp = (ls[0],ls[1],ls[2],ls[3],ls[4],ls[5],ls[6],ls[7],ls[8],ls[9],ls[10],ls[11],ls[12],\
                    ls[13],ls[14],ls[15],ls[16],ls[17],ls[18],ls[19],ls[20],ls[21])
            values.append(tmp)
            del tmp
            print values
        return values


    def insert(self,SqlFile,DataSource):
	"""
	    批量插入数据，可以使用executemany()方法也可以循环使用execute()
	"""
        print "come to insert"
        cursor = self.GetConnect()
        values = self.getValues(DataSource)
	#sqlStr = open(SqlFile,'r').read(
        print '====================================='
        for sqlStr in  SqlFile:
            print "sql in insert is :",sqlStr
            values = self.getValues(DataSource)
            print "values is :\n",values
            affected = cursor.executemany(sqlStr,values)
            print "affected in insert is :",affected
            self.conn.commit()
            print '================='
        cursor.close()
        self.conn.close()
    


"""
	1:mysql	sqlserver
	2.sqlString
	3.dataFile
	4.执行查询的种类    1，查找 2，更新 3，添加
"""

if __name__== "__main__":
    
    try:
        len = len(sys.argv)
        print "parameter's length is :",len
        #67.15:6030  hotel_mapping
        Mysql = MysqlDB(host_67,port_67,user_67,password_67,dbname_67)
        #76.15 流水表
        #Mysql = MysqlDB(host,port,user,password,dbname)
        #data = sys.argv[1]
        #mysql.getValues(data)
        
        if len == 4:
            Type = sys.argv[1]
            SqlFile = sys.argv[2]
            DataSource = sys.argv[3]
            ##两天以后的三天的数据GenerateSql(2,3)
            SqlFile = GenemajiaSql(1,2)
            # SqlFile = GenerateSql(1,5)
            print "============== main ==============="
            for i in SqlFile:
                print i,'\n'
            #SqlFile = GenemajiaSql(6,9)
            #SqlFile = GenerateSql(1,5)
            #Mysql = MysqlDB(HOST,PORT,USER,PASSWORD,DBNAME)
            #Mysql = MysqlDB(host,port,user,password,dbname)
            Mysql.insert(SqlFile,DataSource)
        elif len == 3 :
            Mysql = MysqlDB(host,port,user,password,dbname)
            type = int(sys.argv[1])
            SqlFile = sys.argv[2]
            if( 1 == type):
                #Mysql = MysqlDB(HOST,PORT,USER,PASSWORD,DBNAME)
                Mysql.search(SqlFile)
            elif 2 == type:
                #Mysql = MysqlDB(HOST,PORT,USER,PASSWORD,DBNAME)
                Mysql.update(SqlFile)
            else :
                pass
        else :
            raise IndexError
    except IndexError:	
        print "\033[35m \t ./Mysql.py 3 sqlFile data \033[0m "
        print "\033[35m \t *********** 参数1：查询方式，1—查询 2—更新 3—插入 \033[0m"
        print "\033[35m	 *********** 参数2：sql语句  参数3：插入数据 \033[0m"







