#!/usr/bin/env python
#-*- coding: utf-8 -*-

import MySQLdb,pymssql
import logging
import traceback
import sys
import time
import datetime
sys.path.append('hotelInvShardMap')
from invShardServer import *

## @desc 获取shotel_id的库存分片
Shard_HOST = '192.168.76.34'
Shard_PORT = 9092

## @desc 库存mysql的ip，PORT为最小的端口号
HOST = '192.168.76.15'
PORT = 6026
USER = 'inv_test_w'
PASSWORD = '123456'
DBNAME = 'hotel_inventory'

## @desc   Mysql数据库的查询器
class MysqlHandler:
    host_ = ''
    port_ = 0
    user_ = ''
    password_ = ''
    dbname_ = ''

    @classmethod
    def InitDB(cls, host, port, user, password, dbname):
        cls.host_ = host
        cls.port_ = port
        cls.user_ = user
        cls.password_ = password
        cls.dbname_ = dbname

    @classmethod
    def Select(cls, selectSql):
        conn = MySQLdb.connect(host = cls.host_, port = cls.port_, user = cls.user_, passwd = cls.password_, db = cls.dbname_)
        cursor = conn.cursor()
        cursor.execute(selectSql)
        rows = cursor.fetchall()
        cursor.close ()
        conn.close ()
        return rows

## @desc    查找shotel所在的库存分片
## @para    shotel_id
## @return  库存分片, 取值范围为[0, 3]
def get_shotel_inv_shard(shotel_id):
    SHotelInventoryShard.SetHost(Shard_HOST, Shard_PORT)
    return SHotelInventoryShard.GetShardId(shotel_id)

## @desc    获取库存的详细数据
## @para    分片id 酒店id sroomid date
## @return
def get_inventory(shard_id, shotel_id, sroom_id, date):
    begin_date = ''
    end_date = ''
    type = 1
    PORT_NEW = PORT + int(shard_id)
    if len(date.split('-')) > 1:
        begin_date = date.split('-')[0]
	end_date = date.split('-')[1]
    else:
        begin_date = end_date = date

    sql_cond = "hotel_id='%s' AND room_type_id='%s' AND" % (shotel_id, sroom_id)
    selectSql = "                                               \
        SELECT  sum_inv_room_id,                                \
                hotel_id,                                       \
                room_type_id,                                   \
                available_amount,                               \
                available_time,                                 \
                datediff(available_time,'1970-1-1') AS days,    \
                begin_time,                                     \
                end_time,                                       \
                inv_status,                                     \
                is_over_booking,                                \
                %d AS full_or_allbuy,                           \
                begin_date,                                     \
                end_date,                                       \
                is_policy_limit AS inv_type_detail              \
        FROM    sum_inv_room                                    \
        WHERE   %s                                              \
                available_time >= '%s'                          \
                AND available_time <= '%s'                      \
        ORDER BY hotel_id, room_type_id, available_time"        \
        % (type, sql_cond, begin_date, end_date)
    MysqlHandler.InitDB(HOST, PORT_NEW, USER, PASSWORD, DBNAME)
    return MysqlHandler.Select(selectSql)

## @desc 获取指定酒店+房型的库存
def main(shotel_id,sroom_id,date):
    shard_id = get_shotel_inv_shard(shotel_id)
    #print 'shard_id:',shard_id
    inv_details = get_inventory(shard_id, shotel_id, sroom_id, date)
    invs = ''
    for d in inv_details:
	invs += '{"hotel_id":"%s","room_id":"%s","amount":%d,"status":%d,"is_over_booking":%d,"start_time":"%s","end_time":"%s","available_date":"%s","start_date":"%s","end_date":"%s","inv_type_detail":"%d","version":"%s"},'\
            % (d[1],d[2],d[3], d[8], d[9], d[6], d[7], d[4], d[11], d[12], d[13], d[0])
	invs += '\n'
    print invs

if __name__ == '__main__':
    try:
	shotel_id = sys.argv[1]
	sroom_id  = sys.argv[2]
	date = sys.argv[3]
        main(shotel_id,sroom_id,date)
    except IndexError:
	print "\033[31m *** sys.argv[1] 查询的shotel_id                        ***\033[0m"
	print "\033[31m *** sys.argv[2] 查询的sroom_id                         ***\033[0m"
	print "\033[31m *** sys.argv[3] 查询的年:月:日 （- 年:月:日）          ***\033[0m"
	print "\033[32m python %s  shotel_id  sroom_id  Y:M:D-Y:M:D \033[0m" % sys.argv[0]
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(e)
        raise
