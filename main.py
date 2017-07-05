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


# id = int(sys.argv[1])
# ci = int(sys.argv[2])
# co = int(sys.argv[3])
hotel_ids = [90000064,101162,2001137,10201019]
# call_ds.main(90000329,1,2)

# call_ds.main(50101002,1,2);

# call_dc_app.main(20101401,1,2)

# call_service_CanBook.process(90101033,1,2)

# call_service.process(90000064,2,3,4)  ## 列表页吐出最低价格库存
# call_service.process(90000745,2,4,4)  ## 列表页吐出最低价格库存

# call_sa.process(90101033,1,2)  ## 列表页吐出最低价格库存
# for i in xrange(0,300):
# call_sa.process(91412068,1,2,4)     ##灰度信用住酒店
#     time.sleep(5)

# call_sa.process(90000064,0,1,1)    # 灰度搜索专用酒店

# call_sa.process(90649140,0,1,4)

# call_sa.process(90679475,0,2,4)    # 线上shard1酒店

# for i in xrange(500):
#     print datetime.datetime.now()
#     print '=='*8
#     call_sa.process(90679475,0,2,4)    # 线上shard1酒店
#     time.sleep(3)

# call_sa.process(90929686,1,2,4)     ##灰度微信新客


# call_sa.process(60101873,1,2,4)     ##灰度微信新客
# call_sa.process(90977622,1,2,4)     ##灰度直连五折测试酒店  信用住

# call_sa.process(90101033,1,2)
# call_sa.process(10101129,1,2)

# call_sa.process(90101033,0,1,1)   ## 列表页吐出最低价格库存
# call_service.process(90101033,0,1,1)   ## 列表页吐出最低价格库存

# call_sa.process(30101023,1,2,1)   ## 快筛项交并集


# call_sa.process(10101466,1,4,4)   ## 库存
# call_sa.process(10101466,1,4,1)   ## 库存
# call_service.process(40101589,1,2,1)   ## 库存

# call_sa.process(30101023,1,2,1)   ## 最低价产品差5毛，微信钱包新用户
# call_service.process(30101023,1,2,1)   ## 最低价产品差5毛

# call_sa.process(50101021,0,1)   ## 灰度到店时间
# call_sa.process(91348508,0,1,1)   ## 灰度到店时间
# call_sa.process(50101021,-1,0,4)   ## 灰度到店时间
# call_sa.process(90048709,-1,0)   ## 灰度到店时间

# call_sa.process(2001137,1,2)     ##测试环境直连酒店


# call_sa.process(91924993,1,2) ## 灰度，直连酒店

# call_sa.process(12001059,13,14)  ## ean酒店
# call_sa.process(90679475,1,2)

# call_sa.process(90000064,2,3)  ## 微信专享
# call_sa.process(90000064,3,4)  ## 微信专享

# call_sa.process(50101002,1,2)  ## 到店时间

# call_sa.process(90101033,1,2)  ## 马甲、五折

# call_sa.process(40101589,1,2) ## 联调酒店

# call_sa.process(40101006,1,2)   ## 北京西苑，闪住信用住
# call_sa.process(2001137,1,2)   ## 闪住信用住

# call_sa.process(30101023,1,2,4)  ## 信用住 — 立减、红包立减、红包返现
#
# call_sa.process(50101012,1,2,4)

# call_sa.process(101338,-1,0)   ## 到店时间（当天订昨天）信用住-红包返现
# call_sa.process(101338,0,1,4)   ## 到店时间（当天订昨天
# call_sa.process(101338,1,2)   ## 到店时间（当天订昨天

# call_sa.process(90000745,1,2) ## 马甲该流程
# call_sa.process(id,ci,co)

# call_service.process(90000745,0,1,4)  #最大入住间数

# call_sa.process(40101006,1,2,4)   ##drr底价、列表页促销金额
# print '\033[35m**\033[0m'*30
# print '\033[35m**\033[0m'*30
# call_service.process(40101006,1,2,4)  ## drr底价、列表页促销金额

# print '\033[35m**\033[0m'*30
# print '\033[35m**\033[0m'*30
#
# call_sa.process(2001137,1,2,4)   ##铂涛测试环境联调

# call_sa.process(90924681,1,2,1)   ##铂涛测试环境联调
# call_sa.process(91924993,0,1,4)   ##铂涛测试环境联调

# call_service.process(90727029,1,2,4)  ##铂涛新会员测试环境

# call_sa.process(516017,1,2,4) ## 铂涛会员灰度环境数据


# call_service.process(50101002,1,2,4)
# call_service.process(90021543,0,1,4)
# call_service.process(101112,1,2,4)
# call_sa.process(90949966,0,1,4)    # 马甲
# call_sa.process(91778835,0,1,4)    # 马甲测试酒店 验价格
# call_sa.process(90931731,0,1,4)    # 促销精确锚定
# call_service.process(90000745,0,1,4)   #90000329   30101023

# for i in xrange(30):
#     time.sleep(5)
#     call_sa.process(91924993,5,6,4)  #返现兜底
#     print "\033[33m===========================\033[0m"
#

# print time.time()
# call_sa.process(90101033,2,3,4)
# call_sa.process(90000329,0,1,4)
# call_sa.process(91778835,2,16,4)

# ———————————————— NB库存接口  ————————————————————
# print "\033[33m================================\033[0m"
start_date = int(time.mktime(time.strptime('2017-05-17','%Y-%m-%d')))
end_date = int(time.mktime(time.strptime('2017-05-18','%Y-%m-%d')))
req = {"mhotelAttr":["30101023-80101019-1078"],
       "start_date":start_date*1000,
       "end_date":end_date*1000,
       "need":True
       }
# for one in req["mhotelAttr"]:
#     rs = one.split("-")
#     mhotels = int(rs[0])
#     print "mhotel",int(mhotels)
#     if len(rs) >= 2:
#         shotels = rs[1].split('|')
#
#         print 'shotels:',[int(x) for x in shotels]
#         if len(rs) >= 3:
#             srooms = rs[2].split('|')
#             print "srooms: ",[int(x) for x in srooms]

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

rateplan = {"MetaMhotel":["90000064-90000822"],
            "payment_type":0,
            "booking_channel":12,
            "sell_channel":12,
            "member_level":15,
            "traceId":3124
           }
nb = call_service.GetRatePlanForNB()
# nb.get_response(rateplan)

# call_sa.process(50401025,1,2,4)
call_sa.process(30101023,1,2,4)
# call_service.process(40101022,1,2,4)
# call_service.process(90000064,1,2,4)
# call_sa.process(91924993,1,2,4)