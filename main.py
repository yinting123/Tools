#-*-coding:utf-8 -*-
#/usr/bin/env python
# __author__ = 'ting.yin'
# import call_ds
import os,sys
import call_dc_app
import call_sa
import call_service
import call_service_CanBook
import time
import call_ds
import time

from datetime import datetime


# ———————————————— NB库存接口  ————————————————————
# print "\033[33m================================\033[0m"
start_date = int(time.mktime(time.strptime('2017-05-17','%Y-%m-%d')))
end_date = int(time.mktime(time.strptime('2017-05-18','%Y-%m-%d')))
req = {"mhotelAttr":["30101023-80101019-1078"],
       "start_date":start_date*1000,
       "end_date":end_date*1000,
       "need":True
       }

# print req
# nb = call_ds.GetInvForNB()
# print type(req)
# nb = call_service.GetInvForNB()
# nb.get_response(req)

# ———————————————— NB库存接口  ————————————————————
start = int(time.mktime(time.strptime("2017-05-08 10:00:00","%Y-%m-%d %H:%M:%S")))
# start = int(time.mktime(time.strptime("2017-06-01","%Y-%m-%d")))
end = int(time.mktime(time.strptime("2017-11-03 10:00:00","%Y-%m-%d %H:%M:%S")))
# end = int(time.mktime(time.strptime("2017-06-08","%Y-%m-%d")))
# print start
# print end
price = {"hotel_base_price_request":["30101023-90000809",],
        "payment_type":1,
        "start_date":start,
        "end_date":end,
        "booking_channel":32,
        "sell_channel":4,
        "member_level":1,
        "traceId":24234234
       }

# nb = call_ds.GetInvForNB()
# print type(req)
nb = call_service.GetPriceForNB()
# nb.get_response(price)

# ———————————————— rp元数据接口  ————————————————————
rateplan = {"MetaMhotel":["90000064-90000822"],
            "payment_type":0,
            "booking_channel":12,
            "sell_channel":12,
            "member_level":15,
            "traceId":3124
           }
nb = call_service.GetRatePlanForNB()
# nb.get_response(rateplan)


# ———————————————— list、detail 接口  ————————————————————
call_sa.process(30101066,1,2,1)

# call_service.process(30101023,1,2,4)

# call_ds.main(90204504,1,2,4)

# call_service.process(30101023,0,1,4)
# call_service.process(2001231,1,2,4)
# call_service.process(90000064,0,1,4)

# canBook = call_service.SearchCanBook()
# canBook.process([50401025,],34,36)
# call_service_CanBook.process(50401025,34,37)
# call_ds.main(50401025,34,36,4)