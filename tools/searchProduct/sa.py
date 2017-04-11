# -*- coding: utf8 -*-

import os
import sys,getopt
import time
from  verify_majia import  *


sys.path.append("..")
sys.path.append("/Users/user/Documents/project/PycharmProjects/call_ds/thrift")
sys.path.append("/Users/user/Documents/project/PycharmProjects/call_ds/gen")
from thrift import Thrift
from thrift.Thrift import TProcessor
from thrift.transport import TTransport,TSocket
from thrift.protocol import TBinaryProtocol, TProtocol
from gen.se.ttypes import *
from gen.cm.ttypes import *
from gen.thriftproxy.ThriftProxy import Client
from ShowResult import *

# HOST = "172.21.27.25"
# HOST = "10.39.18.58"
HOST = "192.168.233.17"
# HOST = "192.168.233.83"
PORT = "5100"


def check_v(ret, str):
    # print "come to print result"
    print 'status:',ret.status.msg
#    print ret.debug_info
    print 'total:',ret.total
    #print ret
    print 'count:',ret.count
#    print 'grandson:',ret.grandson
#     print ret
    global count;
    count = 0

    show = ShowResult(req,ret)
    show.Product()
    # show.statics()



def check(ret, str):
    for op,args in opts:
        if op == '-h':
            print "usage: \n\t-v: print detail info\n\t-h: print this help"
            sys.exit()
        if op == '-v':
            print ret
    if ret is None:
        print "fail:" + str
    else:
        print "succ:" + str

def  process(id,CI,CO):#page_index):
    try:

        #socket = TSocket.TSocket('10.39.18.58', 5100)
        ##socket = TSocket.TSocket('172.21.106.26', 5100)
        #socket = TSocket.TSocket('192.168.233.17', 5100)
        ##socket = TSocket.TSocket('10.35.15.124', 5100)
        ##socket = TSocket.TSocket('192.168.233.17', 5100)
        #socket = TSocket.TSocket('192.168.76.43', 5101)
        #socket = TSocket.TSocket('172.21.27.25', 5100)
        socket = TSocket.TSocket(HOST, PORT)
        #socket = TSocket.TSocket('192.168.35.37', 5555)
        #socket = TSocket.TSocket('10.39.18.58', 5100)
        transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = Client(protocol)
        transport.open()
        global req
        req = InnerSearchRequest()
        req.inner_search_type = 1
        # req.inner_search_type = 4
        req.hotel_attr = HotelAttribute()



        #eq.hotel_attr.return_has_breakfasts_hotel = 3
        #eq.hotel_attr.return_has_xianfu_hotel = 1
        req.hotel_attr.return_no_product_hotel = 1
        # req.hotel_attr.need_hotel_without_service = 1
        #eq.hotel_attr.return_has_yufu_hotel = 0
        req.hotel_attr.price_sub_coupon = 1
        req.hotel_attr.facility_ids = []
        #eq.hotel_attr.facility_ids.append(100000208)



        req.hotel_attr.fast_filter_ids = []
        #eq.hotel_attr.fast_filter_ids.append(100000001)

        req.hotel_attr.mhotel_ids = []
        #eq.hotel_attr.mhotel_ids.append(101201)
        #req.hotel_attr.mhotel_ids.append(mhotel_id)
        req.hotel_attr.mhotel_ids.append(id)
        print "in request : mhotel_id :%s "%req.hotel_attr.mhotel_ids
        #eq.hotel_attr.mhotel_ids.append(90971639)

        req.hotel_attr.hotel_brand_id = []
        #eq.hotel_attr.hotel_brand_id.append(32) #5
        #req.hotel_attr.hotel_brand_id.append(47) #1
        #req.hotel_attr.hotel_brand_id.append(6) #1
        #req.hotel_attr.hotel_brand_id.append(547) #2

        #eq.hotel_attr.hotel_brand_id.append(374)
        #eq.hotel_attr.hotel_brand_id.append(40)
        #eq.hotel_attr.hotel_brand_id.append(29312)
                #eq.hotel_attr.hotel_brand_id.append(17762)
        #eq.hotel_attr.hotel_brand_id.append(7494)
        #eq.hotel_attr.hotel_brand_id.append(104)
        #eq.hotel_attr.hotel_brand_id.append(621)
        #eq.hotel_attr.hotel_brand_id.append(65)
        #eq.hotel_attr.hotel_brand_id.append(29156)
        #eq.hotel_attr.hotel_brand_id.append(21)
        #eq.hotel_attr.hotel_brand_id.append(31)
        #eq.hotel_attr.hotel_brand_id.append(39)
        #eq.hotel_attr.hotel_brand_id.append(29154)


                #req.hotel_attr.return_assemble = []
        #req.hotel_attr.return_assemble.append(0)

        #eq.hotel_attr.return_has_yufu_hotel = 0
        #eq.hotel_attr.return_has_timerush_product_hotel = 0
        #eq.hotel_attr.keyword = "如家集团"
        #eq.hotel_attr.keyword = "鸟巢"
        #eq.hotel_attr.keyword = "如家"
        #req.hotel_attr.keyword = keyword#"王府井如家"#双床"


        #eq.room_attr = RoomAttribute()
        #eq.room_attr.bed_large_types = []#req.room_attr.bed_large_types.append(36)
        #req.room_attr.bed_large_types.append(37) #双床

        req.product_attr = ProductAttribute()
        #req.product_attr.half_discount_promotion = 3

        req.product_attr.hong_bao_records = []
        # 红包 3-9
        hong_bao_records = HongbaoRecord()
        # hong_bao_records.record_id =
        # hong_bao_records.recharge_type =
        hong_bao_records.tag = 0
        hong_bao_records.face_value = 50
        hong_bao_records.valid_date = "2016-11-27 12:00:00"
        hong_bao_records.activity_id = 201506054 #15082701
        hong_bao_records.status = 1

        # req.product_attr.hong_bao_records.append(hong_bao_records)





        req.product_attr.return_has_resale_hotel = 1

        req.product_attr.cooperation_type = []
        #req.product_attr.cooperation_type.append(1)
        # req.product_attr.searchFrom = 2
        req.product_attr.has_zydj = 1
        #req.product_attr.majia_zydj_switch = 31
        # req.product_attr.discount_method = 3
        req.product_attr.has_majia = True
        #req.product_attr.majia_zydj_switch =
        #req.product_attr.hong_bao_records = []
        #hong_bao_records = HongbaoRecord()
        #hong_bao_records.face_value = 100
        #hong_bao_records.activity_id = 2015081409
        #hong_bao_records.status =1
        #hong_bao_records.activity_channel = []
        #activity_channel = ActivityChannel()
        #activity_channel.type = 2
        #activity_channel.order_form_ids = []
        #activity_channel.order_form_ids.append(50003)
        #activity_channel.order_form_ids.append(501)
        #activity_channel.order_form_ids.append(50)
        #activity_channel.order_form_ids.append(501)
        #activity_channel.order_form_ids.append(50)
        #activity_channel.order_form_ids.append(501)
        #activity_channel.order_form_ids.append(50)
        #activity_channel.order_form_ids.append(501)
        #activity_channel.order_form_ids.append(50)
        #hong_bao_records.activity_channel.append(activity_channel)
        ##hong_bao_records.is_check_in_abs_valid = 1
        ##        hong_bao_records.check_in_abs_date_from = '2016-05-18 10:00:00'
        ##        hong_bao_records.check_in_abs_date_to = '2016-05-25 10:00:00'
        #        hong_bao_records.valid_date = '2016-05-25 10:00:00'
        #req.product_attr.hong_bao_records.append(hong_bao_records)

        # req.hotel_attr.only_consider_salable = False
        req.product_attr.filter_conditions = []
        # fc = FilterCondition()
        # fc.type = 11
        # fc.use_or_not = 1
        # fc.apply_level = 2;
        # fc.filter_value = 1;
        # req.product_attr.filter_conditions.append(fc)
        # req.only_consider_salable = False
        print "======================="
        # if fc.apply_level ==1:
        #     if fc.filter_value ==1 :
        #         print "产品过滤，艺龙开发票"
        #     elif fc.filter_value == 2:
        #         print "产品过滤，酒店开发票"
        # elif fc.apply_level ==2:
        #     if fc.filter_value ==1 :
        #         print "酒店过滤，艺龙开发票"
        #     elif fc.filter_value == 2:
        #         print "酒店过滤，酒店开发票"
        # print "======================="
        print req.product_attr.filter_conditions

        req.product_attr.use_day_promotion = 1
        req.product_attr.is_new_hongbao = 1
        req.product_attr.return_noinv_or_noprice_product = 1
        #eq.product_attr.return_has_memberbenefits_hotel = 1
        #eq.product_attr.list_product_info = ListProductInfo()
        #eq.product_attr.list_product_info.return_min_price_product = 11
        #req.product_attr.list_product_info.need_sorted_top_product =1
        #req.product_attr.price_pair = []
        #price_pair = PricePair()
        #price_pair.min = 500 #297
        #price_pair.max = 99999
        #req.product_attr.price_pair.append(price_pair)
        req.product_attr.stay_date = StayDate()
        req.product_attr.stay_date.check_in = time.time()+86400*CI
        req.product_attr.stay_date.check_out = time.time()+86400*CO
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
        #eq.page_rank_attr.flow_id = 23
        #req.page_rank_attr.feature_policy_ids =[]
        #eq.page_rank_attr.feature_policy_ids.append(2016)
        #eq.page_rank_attr.feature_policy_ids.append(6)
        #eq.page_rank_attr.sorting_method = 7 #0默认poi阶梯排序，2距离，距离升序；
        #req.page_rank_attr.sorting_direction = 1
        #req.page_rank_attr.sort_order_id = 0
        #req.page_rank_attr.sort_policys = []
        #sort_policy = SortPolicy()
        #sort_policy.sort_item = 5
        #sort_policy.sort_item_policy = 1
        #req.page_rank_attr.sort_policys.append(sort_policy)

        req.price_sub_coupon = True

        req.caller_attr = CallerAttribute()
        req.caller_attr.ip = "192.168.1.1"
        req.caller_attr.SearchFrom = 1
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

        req.customer_attr.request_origin = 3

        #req.customer_attr.proxy_id= 'AP0000202'#'AP0011893'#'ZD'
        req.customer_attr.proxy_id= 'AP0011893'# 'AP0048611' #'AP0011893'#'ZD'
        req.customer_attr.order_id= 50 # 5999
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
        #eq.user_info.idfa = '352443060457518||3524E3010407598'
        #eq.user_info.idfa = '165808d5-2f85-476b-846b-7adaea70587b'
        #eq.user_info.idfa = 'f4a64958-d17b-4356-9b8b-e199a39e1de3'
        #eq.user_info.idfa = 'e6f63a2c-7616-47da-9241-644bb924f93d'
        #eq.user_info.idfa = '357513050484667||3575E3010404697'
        #eq.user_info.idfa = '353115059584903||3531E5019504993'
        req.user_info.geo_info = GeoInfo()
        #eq.user_info.geo_info.geo_longitude = 116.373989
        #eq.user_info.geo_info.geo_latitude = 39.89585

        #eq.user_info.geo_info.geo_longitude = 116.5632553
        #eq.user_info.geo_info.geo_latitude = 40.07008124
        #eq.user_info.geo_info.geo_longitude = 116.4677322 #国贸
        #eq.user_info.geo_info.geo_latitude = 39.91606155
        #eq.user_info.geo_info.geo_longitude = 121.496951 #上海外滩
        #eq.user_info.geo_info.geo_latitude = 31.241647

        req.rec_attr = RecommendAttribute()
        #eq.rec_attr.return_talent_recommend = 1
        #eq.rec_attr.rec_result = 1
        #eq.rec_attr.hotel_num = 20
        #req.rec_attr.rec_return_num_only = 0
        # ===========================
        ## 信用住参数
                # 产品、酒店筛选
        req.hotel_attr.return_assemble = []
        # req.hotel_attr.return_assemble.append(7)
        # req.hotel_attr.return_assemble.append(8)

         # 信用住
        # credit = UserCreditLiveInfo()
        # credit.flash_live_filter = False # False ,True             #闪住
        # credit.credit_live_filter = True           #信用住
        # credit.credit_value_live_filter = False #True #False     #是否额度过滤
        # credit.user_credit_value = 100               #额度
        # credit.flash_live_period = 3                #闪住通道
        # credit.credit_live_period = 2               #信用住通道
        # req.product_attr.order_by_user_credit_filter = credit
        #
        # # 预定时间
        # # req.customer_attr.booking_datetime = 1478765280  # 2016-11-10
        #
        # # 五折
        # # req.product_attr.discount_method = 3
        # # 转让房
        # req.product_attr.return_has_resale_hotel = 1
        # # 列表页
        # req.inner_search_type = 4
        # req.geo_attr.region_id = 301#101

        # 信用住 end
        # ===========================

        ret = client.SearchInner(req)

        check_v(ret, "SearchInner")

        # verify_majia(ret)


        transport.close()
        return ret
        #print "request is :%s"%req
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
