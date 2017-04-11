__author__ = 'ting.yin'

#-*-coding:utf-8-*-
import sys
import math
sys.path.append("/Users/user/Documents/project/PycharmProjects/call_ds/gen/")
# from cm.ttypes import  *

def filter(res):
    for detail in res.hotels_details:
        for room in detail.room_types:
            for product in room.products:
                flag = filterWeChat(product)
                if flag :
                    print "shotel_id: ",product.shotel_id
                    print "sroom_id: ",product.sroomtype_id
                    print "rp_id: ",product.rateplan.rateplan_id


def filterWeChat(product):
    rp = product.rateplan
    bk = rp.booking_channel
    if bk & pow(2,10) != 0 and \
          bk & pow(2,1) ==0 and\
            bk & pow(2,4) ==0:
        return True
