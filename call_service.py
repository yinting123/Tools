#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys,getopt
import time
import init,random,uuid

from call_sa import *
from ShowResult import  *

sys.path.append("./gen-py/")

from thrift import Thrift
from thrift.Thrift import TProcessor
from thrift.transport import TTransport,TSocket
from thrift.protocol import TCompactProtocol,TBinaryProtocol, TProtocol
from se.ttypes import *
from cm.ttypes import *
from dss.ttypes import *
from dsservice.ttypes import *
from dynamic_search.ttypes import *
from dsservice.DSServiceProxy import Client

# HOST = '192.168.233.17'
# HOST = '192.168.233.2'
# HOST = '192.168.35.17'
# HOST = '192.168.35.30'
HOST = '192.168.233.83'
# HOST = '192.168.35.17'
# HOST = '192.168.35.21'
# HOST = 'goodsservicenb.vip.elong.com'
# HOST = '172.21.106.26'
# HOST = '192.168.210.52'
PORT = 5400
# PORT = 5401
# PORT = 5407


class GetInvForNB():
    """给NB提供的查询库存以及立即确认的接口"""
    def __init__(self):
        return

    def build_request(self,dictreq):
        req = GetInvAndInstantConfirmRequest()
        req.mhotel_attr = []
        for one in dictreq["mhotelAttr"]:
            rs = one.split("-")
            mhotel = MhotelAttr()
            mhotels = int(rs[0])
            mhotel.mhotel_id = mhotels
            if len(rs) >= 2:
                shotels = rs[1].split('|')
                mhotel.shotel_attr = []
                for sh in shotels:
                    shotel = ShotelAttr()
                    shotel.shotel_id = int(sh)
                    if len(rs) >= 3:
                        srooms = rs[2].split('|')
                        shotel.sroom_ids = [int(x) for x in srooms]
                    mhotel.shotel_attr.append(shotel)
            req.mhotel_attr.append(mhotel)

        req.start_date = dictreq["start_date"]
        req.end_date = dictreq["end_date"]
        req.need_instant_confirm = dictreq["need"]
        # req.order_from = 1
        req.search_from = 3
        # print req
        return req

    def get_connect(self):
        print ("HOST:",HOST,"port:",PORT)
        socket = TSocket.TSocket(HOST, PORT)
        transport = TTransport.TFramedTransport(socket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)
        return transport, client

    def get_response(self,dictreq):
        req = self.build_request(dictreq)
        transport, client = self.get_connect()
        transport.open()
        res = client.GetInvAndInstantConfirm(req)
        transport.close()

        self.handle(res)
        return

    def handle(self,res):
        result = ShowDSResult(res)
        result.ShowInvForNB()

class GetPriceForNB():
    """NB 元数据模式"""
    def __init__(self):
        pass

    def build_request(self,req):
        request = GetBasePrice4NbRequest()
        request.hotel_base_price_request = []
        for item in req["hotel_base_price_request"]:
            mhotel_id = int(item.split("-")[0])
            print mhotel_id
            base_info = HotelBasePriceRequest()
            base_info.mhotel_id = mhotel_id
            if len(item.split("-")) > 1:
                base_info.shotel_id =  int(item.split("-")[1])
            request.hotel_base_price_request.append(base_info)
        request.payment_type = req["payment_type"]
        request.start_date = req["start_date"]
        request.end_date = req["end_date"]
        request.booking_channel = req["booking_channel"]
        request.sell_channel = req["sell_channel"]
        request.member_level = req["member_level"]
        traceId = uuid.uuid1()
        print traceId
        request.traceId = str(traceId )
        return request

    def create_connection(self):
        print ("HOST:", HOST, "port:", PORT)
        socket = TSocket.TSocket(HOST, PORT)
        transport = TTransport.TFramedTransport(socket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)
        return transport, client

    def get_response(self,dictreq):
        req = self.build_request(dictreq)
        transport, client = self.create_connection()
        transport.open()
        res = client.getMetaPrice4Nb(req)
        transport.close()
        self.handle(res)
        return

    def handle(self,res):
        # print res
        print res.return_msg
        result = ShowDSResult(res)
        result.showPriceForNB()

class GetRatePlanForNB():
    def build_message(self,rp):
        request = GetBaseRatePlanDRRGiftRequest()
        metaMhotel = []
        for i in xrange(len(rp["MetaMhotel"])):
            mhotel = rp["MetaMhotel"][i].split("-")[0]
            hotel = MetaMhotel()
            hotel.mhotel_id = int(mhotel)
            if len(rp["MetaMhotel"][i].split("-")) > 1:
                shotel = rp["MetaMhotel"][i].split("-")[1]
                shotels = shotel.split(",")
                hotel.shotel_id = [int(x) for x in shotels]
            metaMhotel.append(hotel)
        request.mhotel = metaMhotel
        request.payment_type = rp["payment_type"]
        request.booking_channel = rp["booking_channel"]
        request.sell_channel = rp["sell_channel"]
        request.member_level = rp["member_level"]
        # request.traceId = rp["traceId"]
        print request
        return request

    def create_connection(self):
        print ("HOST:", HOST, "port:", PORT)
        socket = TSocket.TSocket(HOST, PORT)
        transport = TTransport.TFramedTransport(socket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)
        return transport, client

    def get_response(self,rp):
        request = self.build_message(rp)

        transport,client = self.create_connection()
        transport.open()
        response = client.getMetaRatePlanDrrGift(request)
        self.handle(response)
        transport.close()

    def handle(self, res):
        # print res
        # print res.return_msg
        print json.dumps(res.mhotel_detail,default=lambda o:o.__dict__,indent= 2,encoding="utf-8",ensure_ascii=False)
        # result = ShowDSResult(res)
        # result.showPriceForNB()

class VerifyPrice():
    """调验价接口进行验价"""
    def __init__(self):
        return


def check_v(ret):
    ret = ret.response
    result = ShowResult(req,ret)
    # print 'result',ret
    print '\033[5;33m---------------    service  ------------------\033[0m'

    print 'status:', ret.status.msg
    # result.ShowRatePlan()
    result.Product()
    result.promotionCash()
    # result.service_product()
    # result.Product()
    print '\033[35m===\033[0m' * 10


def build_req(id,CI,CO):
        req_v5 = DSSInnerSearchHotel()
        req_v5.mhotel_id_attr = []
        mhotel_ids = HotelIdAttr()
        mhotel_ids.mhotel_id = id
        mhotel_ids.attr = 1
        #mhotel_ids1 = HotelIdAttr()
        #mhotel_ids1.mhotel_id = 50101002
        #mhotel_ids2 = HotelIdAttr()
        #mhotel_ids2.mhotel_id = 20101401

        #req_v5.mhotel_id_attr.append(mhotel_ids1)
        #req_v5.mhotel_id_attr.append(mhotel_ids2)
        req_v5.mhotel_id_attr.append(mhotel_ids)
        req_v5.is_list_detail = True
        # req_v5.traceId = "abcdefabcdef"
        global req
        req = InnerSearchRequest()
        #eq.inner_search_type = 1
        req.inner_search_type = 4
        req.hotel_attr = HotelAttribute()
        #eq.hotel_attr.return_has_breakfasts_hotel = 3
        #eq.hotel_attr.return_has_xianfu_hotel = 1
        req.hotel_attr.return_no_product_hotel = 1
        req.hotel_attr.need_hotel_without_service = 1
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
        #print "in request : mhotel_id :%s "%req.hotel_attr.mhotel_ids
        req.hotel_attr.mroom_selected = []
        roomSelected = RoomSelected()
        roomSelected.select_room_ids = []
        #roomSelected.select_room_ids.append(1055)
        req.hotel_attr.mroom_selected.append(roomSelected)

        #eq.hotel_attr.mhotel_ids.append(90971639)

        req.hotel_attr.hotel_brand_id = []
        #eq.hotel_attr.hotel_brand_id.append(32) #5
        #req.hotel_attr.hotel_brand_id.append(47) #1
        #req.hotel_attr.hotel_brand_id.append(6) #1
        #req.hotel_attr.hotel_brand_id.append(547) #2
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
        req.product_attr.searchFrom = 3
        req.product_attr.has_zydj = 1
        #req.product_attr.majia_zydj_switch = 31
        # req.product_attr.discount_method = 3
        req.product_attr.return_freesale_msg = 1
        #req.product_attr.has_majia = True
        #req.product_attr.majia_zydj_switch =
        req.product_attr.hong_bao_records = []
        hong_bao_records = HongbaoRecord()
        hong_bao_records.face_value = 30
        hong_bao_records.activity_id = 201506054
        hong_bao_records.status =1
        hong_bao_records.valid_date = '2016-12-25 10:00:00'
        hong_bao_records.hongbao_full_back_rule = HongbaoFullBackRule()
        hong_bao_records.hongbao_full_back_rule.full_amount = 200
        hong_bao_records.hongbao_full_back_rule.back_amount = 50
        #hong_bao_records.activity_channel = []
        #activity_channel = ActivityChannel()
        #activity_channel.type = 2
        #activity_channel.order_form_ids = []
        #activity_channel.order_form_ids.append(50003)
        ##hong_bao_records.is_check_in_abs_valid = 1
        ##        hong_bao_records.check_in_abs_date_from = '2016-05-18 10:00:00'
        ##        hong_bao_records.check_in_abs_date_to = '2016-05-25 10:00:00'
        req.product_attr.hong_bao_records.append(hong_bao_records)


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
        req.product_attr.stay_date.check_in = int(time.time())+86400*CI
        req.product_attr.stay_date.check_out = int(time.time())+86400*CO
        #req.product_attr.product_type = []
        #req.product_attr.product_type.append(6)
        #req.product_attr.product_type.append(1)
        #req.product_attr.product_type.append(5)
        #req.product_attr.product_type.append(7)
        req.product_attr.sell_channel = []
        #eq.product_attr.sell_channel.append(1)
        req.product_attr.promotion_channel_code = '1041'#'0000'#web0000
        #Ceq.product_attr.fil er_conditions = []
        #filter = FilterCondition()
        #filter.type = 13
        #filter.use_or_not = 1
        #filter.apply_level = 2
        #req.product_attr.filter_conditions.append(filter)

        req.geo_attr = GeoAttribute()
        #req.geo_attr.language = "cn"
        #req.geo_attr.geo_type = 1
        #req.geo_attr.nearby = NearBy()
        #req.geo_attr.nearby.center = Location()
        #req.geo_attr.nearby.radius = 5000
        #req.geo_attr.nearby.center.latitude = 39.974035#39.997894# 39.939456
        #req.geo_attr.nearby.center.longitude = 116.496313
        #req.geo_attr.region_id = 101
        #eq.geo_attr.district_id = 25798
        #eq.geo_attr.district_type = 2 #1商圈

        req.page_rank_attr = PageRankAttribute()
        #req.page_rank_attr.page_index = page_index
        req.page_rank_attr.page_index = 0
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

        req.caller_attr = CallerAttribute()
        req.caller_attr.ip = "192.168.1.1"
        #req.caller_attr.old_filter =1
        req.caller_attr.channel = '1northbound'#MIS = 0, WEB = 1, NBAPI = 3, MOBILE = 4, ALL = 100
        req.caller_attr.SearchFrom = 2#'web'
        #req.caller_attr.is_debug = 1
        req.caller_attr.request_origin = 3#3为APP
        #req.caller_attr.trace_id = "abcdef-abcdef"

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
        #req.customer_attr.booking_date = 1474124400 + 1
        #int(time.time())

        #req.customer_attr.proxy_id= 'AP0000202'#'AP0011893'#'ZD'
        req.customer_attr.proxy_id= 'A06'
        #req.customer_attr.order_id= 1001
        req.customer_attr.order_id= 50002
        #eq.customer_attr.member_level= 0
        #eq.customer_attr.botao_customer_level= 2
        #eq.customer_attr.use_botao_promotion= 1
        #req.customer_attr.booking_channel = []
        #req.customer_attr.booking_channel.append(1)
        #req.customer_attr.booking_channel.append(3)
        #req.customer_attr.booking_channel.append(5)
        #req.customer_attr.booking_channel.append(7)

        req.return_attr = ReturnAttribute()
        #eq.return_attr.return_static_info_level = 2
        req.return_attr.return_products = 1
        req.return_attr.return_rateplan_info = 1
        #req.return_attr.return_hotel_static_info = 1
        req.return_attr.return_hotel_id_only = 0

        req.user_info = UserInfo()
        #eq.user_info.idfa = '352443060457518||3524E3010407598'
        #eq.user_info.idfa = '165808d5-2f85-476b-846b-7adaea70587b'
        #eq.user_info.idfa = 'f4a64958-d17b-4356-9b8b-e199a39e1de3'
        #eq.user_info.idfa = 'e6f63a2c-7616-47da-9241-644bb924f93d'
        #eq.user_info.idfa = '357513050484667||3575E3010404697'
        #eq.user_info.idfa = '353115059584903||3531E5019504993'
        req.user_info.geo_info = GeoInfo()

        req.rec_attr = RecommendAttribute()

        
        return req,req_v5


def  process(id,CI,CO,type):
    try:
        socket = TSocket.TSocket(HOST, PORT)
        transport = TTransport.TFramedTransport(socket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)
        transport.open()
        req,req_v5 = build_req(id, CI, CO)
        req = build_message(id,CI,CO,type)
        # req.inner_search_type = 4
        # print "request:\n",req
        ret = client.SearchInner2(req, req_v5)
        check_v(ret)
        transport.close()
        return ret
    except Thrift.TException, tx:
        print "%s" % (tx.message)

#opts, args = getopt.getopt(sys.argv[1:], "hv")
#while 1:
if __name__ == '__main__':
    id = 90000745 # int(sys.argv[1])
    ci = 0    # int(sys.argv[2])
    co = 1    # int(sys.argv[3])
    process(int(id), ci, co,4)
