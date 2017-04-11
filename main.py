__author__ = 'ting.yin'
#-*-coding:utf-8 -*-

# import call_ds
import os,sys
import call_dc_app
import call_sa
import call_service
import call_service_CanBook
import time,datetime
import call_ds


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

# call_sa.process(30101023,1,2)  ## 信用住 — 立减、红包立减、红包返现

# call_sa.process(50101002,1,2)

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

# call_service.process(90727029,1,2,4)  ##铂涛新会员测试环境

# call_sa.process(516017,1,2,4) ## 铂涛会员灰度环境数据


# call_sa.process(92047490,0,1,4)
# call_sa.process(91924993,0,1,4)    # 促销精确锚定
# call_sa.process(90000329,0,1,4)   #90000329   30101023

# call_sa.process(10101323,1,2,1)  #返现兜底
#

call_sa.process(10101323,0,7,4)

# ———————————————— NB库存接口  ————————————————————
# print "\033[33m================================\033[0m"
#
req = {"mhotelAttr":["10101323"],
       "start_date":1490284800000,
       "end_date":1505750400000,
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

# nb = call_ds.GetInvForNB()
nb = call_service.GetInvForNB()
nb.get_response(req)
# ———————————————— NB库存接口  ————————————————————

