# -*- coding: utf8 -*-

import os
import sys,getopt
import time
import init
import json

from thrift import Thrift
from thrift.Thrift import TProcessor
from thrift.transport import TTransport,TSocket
from thrift.protocol import TBinaryProtocol, TProtocol,TCompactProtocol
from se.ttypes import *
from cm.ttypes import *
from thriftproxy.ThriftProxy import Client
from utils.Format_time import *
from ShowResult import *

# HOST = "sa-mapi.vip.elong.com"
# HOST = "172.21.27.25"
# HOST = "10.39.18.58"
HOST = "192.168.233.17"
# HOST = "192.168.210.52"
# HOST = "192.168.233.83"
# HOST = "192.168.233.2"
# HOST = "192.168.210.52"
# HOST = "192.168.233.83"
PORT = 5100


def check_v(ret, str):
    # print "come to print result"
    print 'status:',ret.status.msg

    print 'total:',ret.total

    print 'count:',ret.count
#    print 'grandson:',ret.grandson
#     print ret
    global count;
    count = 0

    # fp = open('result.txt','w+')
    # fp.write(json.dumps(ret))
    # fp.close()
    show = ShowResult(req,ret)
    if req.inner_search_type == 1:
        show.service_product()
        show.statics()
        # show.Product()
        # show.hasMajia()
        # show.minPrice()
    elif req.inner_search_type == 4:
        # print ret
        # show.minPrice()
    # show.filter()
        show.Product()
        # show.singleProduct()
        # show.updateInvSecond()
    # show.hasCredit()


def build_message(id,CI,CO,type):
    global req
    req = InnerSearchRequest()

    # req.inner_search_type = 1
    # req.inner_search_type = 4
    req.hotel_attr = HotelAttribute()

    # req.hotel_attr.keyword = "北京饭店"

    #eq.hotel_attr.return_has_breakfasts_hotel = 3
    #eq.hotel_attr.return_has_xianfu_hotel = 1
    req.hotel_attr.return_no_product_hotel = 1
    # req.hotel_attr.need_hotel_without_service = 1
    #eq.hotel_attr.return_has_yufu_hotel = 0
    req.hotel_attr.price_sub_coupon = 1
    req.hotel_attr.facility_ids = []
    #eq.hotel_attr.facility_ids.append(100000208)

    # 快筛项
    # 只看优惠: 0:今日特价  1：可用红包  2:返现
    # 3:五折限购 4:限时抢 5:周边抢 6: 转让房
    req.hotel_attr.return_assemble = []
    # req.hotel_attr.return_assemble.append(0)
    # req.hotel_attr.return_assemble.append(1)
    # req.hotel_attr.return_assemble.append(2)
    # req.hotel_attr.return_assemble.append(3)
    # req.hotel_attr.return_assemble.append(4)
    # req.hotel_attr.return_assemble.append(5)
    # req.hotel_attr.return_assemble.append(6)

    # 特权服务
    # 0:闪住  1：信用住
    req.hotel_attr.privilege_return_assemble = []
    # req.hotel_attr.privilege_return_assemble.append(0)
    # req.hotel_attr.privilege_return_assemble.append(1)

    req.hotel_attr.fast_filter_ids = []
    # eq.hotel_attr.fast_filter_ids.append(100000001)


    #eq.hotel_attr.mhotel_ids.append(101201)
    #req.hotel_attr.mhotel_ids.append(mhotel_id)
    # req.hotel_attr.mhotel_ids.append(id)
    #eq.hotel_attr.mhotel_ids.append(90971639)



            #req.hotel_attr.return_assemble = []
    #req.hotel_attr.return_assemble.append(0)

    # 过滤高定高反酒店
    # req.hotel_attr.return_has_gdgf_hotel = True

    #  @des ProductAttr
    req.product_attr = ProductAttribute()
    #req.product_attr.half_discount_promotion = 3

    req.product_attr.return_shopper_product = True
    # 返回二手房产品
    req.product_attr.return_has_resale_hotel = 1

    req.product_attr.cooperation_type = []
    req.product_attr.promotion_black_list = []
    black_list = PromotionBlackList()
    black_list.promotion_type = 1
    req.product_attr.promotion_black_list.append(black_list)


    #  11：发票模式  12：转让房  13：钟点房  14：闪住  15：信用住
    #  16：担保    17：景酒  18：马甲   19：返现增强
    # req.hotel_attr.only_consider_salable = False
    req.product_attr.filter_conditions = []
    fc = FilterCondition()
    # fc.type, fc.use_or_not, fc.filter_value, fc.apply_level = 14, 1, 2, 2
    fc.type, fc.use_or_not, fc.apply_level = 14, 1, 2
    # req.product_attr.filter_conditions.append(fc)


    req.product_attr.use_day_promotion = 1
    req.product_attr.return_noinv_or_noprice_product = 1
    #eq.product_attr.return_has_memberbenefits_hotel = 1
    #eq.product_attr.list_product_info = ListProductInfo()
    #eq.product_attr.list_product_info.return_min_price_product = 11
    #req.product_attr.list_product_info.need_sorted_top_product =1

    req.product_attr.stay_date = StayDate()
    req.product_attr.stay_date.check_in = int(time.time())+86400*CI
    req.product_attr.stay_date.check_out = int(time.time())+86400*CO
    # req.product_attr.stay_date.check_in = time.time()+86400*CI
    # req.product_attr.stay_date.check_out = time.time()+86400*CO
    req.product_attr.product_type = []
    #eq.product_attr.product_type.append(15)
    #req.product_attr.product_type.append(1)
    #req.product_attr.product_type.append(5)
    #req.product_attr.product_type.append(7)
    req.product_attr.sell_channel = []
    #eq.product_attr.sell_channel.append(1)
    req.product_attr.promotion_channel_code = '1041'#'0000'#web0000

    req.geo_attr = GeoAttribute()
    #req.geo_attr.language = "cn"
    #req.geo_attr.geo_type = 1
    #req.geo_attr.nearby = NearBy()
    #req.geo_attr.nearby.center = Location()
    #req.geo_attr.nearby.radius = 5000
    #req.geo_attr.nearby.center.latitude = 39.974035#39.997894# 39.939456
    #req.geo_attr.nearby.center.longitude = 116.496313
    req.geo_attr.region_id = 101
    #eq.geo_attr.district_id = 25798
    #eq.geo_attr.district_type = 2 #1商圈
    #eq.geo_attr.poi_id = 13904468 #张裕爱斐堡国际酒庄
    #eq.geo_attr.poi_id = 13690245 #北京工人体育场
    #eq.geo_attr.poi_id = 13681139 #北京大学
    #eq.geo_attr.poi_id = 51032911 #故宫
    #eq.geo_attr.poi_id = 13881372 #北京协和医院东
    #eq.geo_attr.poi_id = 128174 #北京站
    #eq.geo_attr.poi_id = 60000067 #国贸

    req.page_rank_attr = PageRankAttribute()
    req.page_rank_attr.page_index = 0
    #req.page_rank_attr.page_index = 0
    req.page_rank_attr.page_size = 100


    req.caller_attr = CallerAttribute()
    req.caller_attr.ip = "192.168.1.1"
    # req.caller_attr.SearchFrom = 2
    # req.caller_attr.SearchFromEnd = 4
    req.caller_attr.onlydebug = 1
    #req.caller_attr.old_filter =1
    # eq.caller_attr.channel = 'mobile'#'web'
    #req.caller_attr.is_debug = 1
    req.caller_attr.request_origin = 3#3为APP

    #铂涛会员
    #req.customer_attr = CustomerAttribute()
    #req.customer_attr.group_info = [];
    #group_info = GroupInfo()
    #group_info.group_id = 3600
    #group_info.elong_level = e_level;
    #req.customer_attribute.append(group_info)

    req.customer_attr = CustomerAttribute()

    #req.customer_attr.group_info = []
    #group_info = GroupInfo()
    #group_info.group_id = 3600
    #group_info.elong_level = e_level;
    #req.customer_attr.group_info.append(group_info)
    #print "in request ,group_info: %s "%req.customer_attr.group_info

    ft = FormatTime()
    req.customer_attr.request_origin = 3
    # req.customer_attr.booking_date = ft.SetTimeToday('03:00:00')  # 2016-11-25 01:00:01
    # req.customer_attr.booking_date = ft.SetTimeToday('05:00:00')  # 2016-11-25 01:00:01

    # req.customer_attr.booking_date = 1480006801  # 2016-11-25 01:00:01
    # req.customer_attr.booking_date = 1480010399  # 2016-11-25 01:59:59
    # req.customer_attr.booking_date = 1480010400  # 2016-11-25 02:00:00
    # req.customer_attr.booking_date = 1480010401  # 2016-11-25 02:00:01
    # req.customer_attr.booking_date = 1480006860  # 2016-11-25 16:00:01
    # req.customer_attr.booking_date = 1480071601  # 2016-11-25 19:00:01
    # req.customer_attr.booking_date = 1480075199  # 2016-11-25 19:59:59
    # req.customer_attr.booking_date = 1480071599  # 2016-11-25 18:59:59
    # req.customer_attr.booking_date = 1480075200  # 2016-11-25 20:00:00
    # req.customer_attr.booking_date = 1480075201  # 2016-11-25 20:00:01


    #req.customer_attr.proxy_id= 'AP0000202'#'AP0011893'#'ZD'
    req.customer_attr.proxy_id= 'AP0011563'#'AP0011563'# 'AP0011893'# 'AP0048611' #'AP0011893'#'ZD'
    req.customer_attr.order_id=  50008 # 5999 60001  50008
    #req.customer_attr.order_id= 50003
    req.customer_attr.member_level= 1
    #eq.customer_attr.botao_customer_level= 2
    #eq.customer_attr.use_botao_promotion= 1
    #req.customer_attr.booking_channel = []
    #req.customer_attr.booking_channel.append(1)
    #req.customer_attr.booking_channel.append(3)
    #req.customer_attr.booking_channel.append(5)
    #req.customer_attr.booking_channel.append(7)

    req.return_attr = ReturnAttribute()
    req.return_attr.return_static_info_level = 1
    req.return_attr.return_products = 1
    req.return_attr.return_rateplan_info = 1
    req.return_attr.return_hotel_static_info = 1
    req.return_attr.return_hotel_id_only = 0

    req.user_info = UserInfo()

    req.user_info.geo_info = GeoInfo()

    req.rec_attr = RecommendAttribute()
    req.rec_attr.rec_result = True

    # req.caller_attr.SearchFrom = 1
    req.product_attr.has_zydj = 1
    req.product_attr.has_majia = True






    # ===========================
    ## 信用住参数
            # 产品、酒店筛选
    # req.hotel_attr.return_assemble = []
    # req.hotel_attr.return_assemble.append(7)
    # req.hotel_attr.return_assemble.append(8)

            # 信用住 请求参数
    credit = UserCreditLiveInfo()
    credit.flash_live_filter = False # False ,True             #闪住
    credit.credit_live_filter = True           #信用住
    credit.credit_value_live_filter = False #True #False     #是否额度过滤
    credit.user_credit_value = 200               #额度
    credit.flash_live_period = 0                #闪住通道
    credit.credit_live_period = 30               #信用住通道
    req.product_attr.order_by_user_credit_filter = credit

            # 五折 参与相容互斥 ，不参与
    req.product_attr.discount_method = 3
    req.product_attr.half_discount_promotion = 3
            # 转让房 吐出转让房 不参与®
    req.product_attr.return_has_resale_hotel = 1


    ##红包
    req.product_attr.is_new_hongbao = 1

    req.product_attr.hong_bao_records = []
        # 红包 3-9
        # tag  0:普通  1：专享   1000：满返
    hong_bao_records = HongbaoRecord()
    # hong_bao_records.record_id =
    # hong_bao_records.recharge_type =
    hong_bao_records.tag = 0
    hong_bao_records.face_value = 30
    hong_bao_records.valid_date = "2017-12-27 12:00:00"
    hong_bao_records.activity_id = 2020000010 #15082701
    hong_bao_records.status = 1

    full_hong_bao = HongbaoFullBackRule()
    full_hong_bao.full_amount = 90
    full_hong_bao.back_amount = 60

    hong_bao_records.hongbao_full_back_rule = full_hong_bao

    # req.product_attr.hong_bao_records.append(hong_bao_records)

    # hongbao end
    # ===========================

    # req.product_attr.return_hotel_ticket_product = True
    # req.product_attr.return_new_botao_member_product = True#False #True

        # 列表、详情
    if type == 1:
        req.inner_search_type = 1
        req.geo_attr.region_id = 101#2201#101
        req.page_rank_attr.page_size = 200
        req.page_rank_attr.page_index = 0
        # req.hotel_attr.mhotel_ids = []
        # req.hotel_attr.mhotel_ids.append(id)

    elif type == 4:
        req.inner_search_type = 4
        req.hotel_attr.mhotel_ids = []
        req.hotel_attr.mhotel_ids.append(id)
        # req.hotel_attr.mhotel_ids.append(50101002)
        # req.hotel_attr.mhotel_ids.append(30101023)

    # print (req)
    return req



def  process(id,CI,CO,type):#page_index):
    try:
        print 'host:',HOST,PORT
        socket = TSocket.TSocket(HOST, PORT)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        # protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)
        transport.open()
        req = build_message(id,CI,CO,type)
        # print json.dumps(req,default=lambda o:o.__dict__)
        ret = client.SearchInner((req))
        print json.dumps(ret,default=lambda o:o.__dict__)
        # check_v(ret, "SearchInner")
        transport.close()
    except Thrift.TException, tx:
        print "%s" % (tx.message)

opts, args = getopt.getopt(sys.argv[1:], "hv")
#while 1:
if __name__ == '__main__':
        global e_level,host;
        try:
                id = int(sys.argv[1])
                ci = int(sys.argv[2])
                co = int(sys.argv[3])

                process(id,ci,co)
        except KeyboardInterrupt:
            pass
#       except Exception as e:
#           logging.error(e)
#           raise
