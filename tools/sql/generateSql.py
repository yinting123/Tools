#!/usr/bin/env python

from time import localtime
from datetime import timedelta,datetime
import sys


def getDeltaDate(day):
    now = datetime.now()
    if day < 0 :
        now -= timedelta(days=day)
    elif day > 0:
        now += timedelta(days=day)
    return now

def GenemajiaSql(days,total):
    strSql = []
    names = []
    for i in range(total):
        names = []
        names.append('mj_app_price_%s'%(strfDate(days+i)))
        names.append('mj_pc_price_%s'%(strfDate(days+i)))
        for name in names:
#            baseStr = "insert into %s\
#                    (checkin_date,elong_mhotel_id,\
#                    elong_mroom_id,pay_type,breakfast_digit,\
#                    ctrip_deal_price,qunar_deal_price,elong_mhotel_name,lowest_term)\
#                    values(%s,%s,%s,%s,%s,%s,%s,%s,1)"\
#                    %(name,strfDate(days+i),'%s','%s','%s','%s','%s','%s','%s')


            baseStr = "insert into %s\
                    (checkin_date,elong_mhotel_id,elong_mhotel_name,\
                    elong_mroom_id,pay_type,breakfast_digit,\
                    ctrip_deal_price,qunar_deal_price,lowest_term,\
                    province,city,address,phone,elong_rp_id,\
                    elong_shotel_id,elong_sroom_id,ctrip_mroom_id,qunar_mhotel_id,\
                    group_id,group_name,supplier_name,elong_href,ctrip_href,qunar_href,\
                    sync_date,update_date,_timestamp)\
                    values(%s,%s,%s,%s,%s,%s,%s,%s,1,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,now(),now(),now())"\
                    %(name,strfDate(days+i),'%s','%s','%s','%s','%s','%s','%s',\
                    '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
            print baseStr
            strSql.append(baseStr)
            del baseStr
    del names
    return strSql

def GenerateSql(days,total):
    strSql = []
    for i in range(total):
        name = "mj_app_price_%s"%(strfDate(days+i))
        baseStr = "insert into %s\
                (check_in,)"
    for i in range(total): 
        name = "center_price_%s"%(strfDate(days+i))
        baseStr = "insert into %s \
                   (checkin_date,checkout_date,elong_mhotel_id,\
                   elong_mroom_id,ctrip_mhotel_id,ctrip_mroom_id,\
                   ctrip_room_id,qunar_mhotel_id,qunar_mroom_id,\
                   pay_type,breakfast,pc_deal_price,app_deal_price,\
                   last_modify_date)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                   %s,%s,%s,now())"\
                   %(name,strfDate(days+i),strfDate(days+i+1)\
                   ,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')
        print baseStr
        strSql.append(baseStr)
    return strSql
    


def strfDate(days):
    needDay = getDeltaDate(days)
    ##print "the format day is :%s"%(datetime.strftime(needDay,"%Y%m%d"))
    return datetime.strftime(needDay,"%Y%m%d")

if __name__ == "__main__":
    delta = int(sys.argv[1])
    total = int(sys.argv[2])
    # GenemajiaSql(delta,total)
    GenerateSql(delta,total)
    #strfDate(delta)
