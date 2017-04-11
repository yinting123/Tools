
#-*-coding:utf-8 -*-
import sys,time,json
import jsonpickle
import md5
import init


from  ShowResult import *

from thrift import Thrift
from thrift.transport import TTransport,TSocket
from thrift.protocol import TCompactProtocol,TBinaryProtocol
from gen.dynamic_search.ttypes import *
# from ttypes import *
from gen.dynamic_search.ProductSearchService import Client


# HOST = "172.21.27.25"
# HOST = "10.39.18.58"
# HOST = "sa-mapi.vip.elong.com"
# HOST = "192.168.35.30"  #——shard_2
HOST = "192.168.233.17"
# HOST = "192.168.35.30"    #——shard_3
# HOST = "192.168.210.52"
# HOST = "192.168.233.2"
# HOST = "192.168.210.52"
# HOST = "192.168.233.83"
PORT = 5800


class GetInvForNB():
    def __init__(self):
        return

    def build_request(self, dictreq):
        req = GetInvAndInstantConfirmRequest()
        req.mhotel_attr = []
        for one in dictreq["mhotelAttr"]:
            rs = one.split("-")
            mhotel = MhotelShotelAttr()
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
        req.order_from = 1
        req.search_from = 3
        print req
        return req

    def get_connect(self):
        socket = TSocket.TSocket(HOST,PORT)
        transport = TTransport.TFramedTransport(socket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)
        return transport, client

    def get_response(self,reqdict):
        req = self.build_request(reqdict)
        transport, client = self.get_connect()
        transport.open()
        res = client.getInvAndInstantConfirm(req)
        transport.close()
        self.handle(res)

    def handle(self,res):
        result = ShowDSResult(res)
        result.ShowInvForNB()


def build_message(id,ci,co,type):
        global request
        request = SearchRequest()

        request.onlydebug = True
        #request.booking_datetime = int(time.time()) + 86400 * ci
        request.checkin_date = int(time.time()) + 86400 * ci;
        request.checkout_date = int(time.time()) + 86400 * co;
        #request.booking_channel = ;
        #request.sell_channel = 127;
        # request.return_has_resale_hotel = 1

        request.searchFrom = 2
        # request.has_zydj = True
        # request.has_majia = True
        request.onlydebug = True
        request.onlymajiadebug = True
        # request.customer_level = 1;
        request.price_sub_coupon = True

        src = "hello"
        m1 = md5.new()
        m1.update(src)
        request.traceId = m1.hexdigest()

        request.mhotel_attrs = []
        # for id in hotel_ids:
        hotels = MHotelAttr()
        hotels.mhotel_id = id
        request.mhotel_attrs.append(hotels)


        list_codes = [43,1,2,3,4,5,6,7,8,9,10,11,28,33,34,35,36,37,38,40,41,42]
        detail_codes = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,\
        30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46]
        # 列表详情
        request.codes = []
        if type == 1:
            codes = list_codes
        elif type == 4:
            codes = detail_codes
        for i in codes :
                request.codes.append(i)

#         FilterCondition 筛选条件
#             apply_level 传1 表示产品过滤
#        type：1, 最小入住天数限制; 2, N间起订;
#             3, 早餐筛选.     filter_value:4, 不含早。1,筛选单早。2,筛选双早 3,筛选3早及以上
#             4, 床型筛选.  5, 支付方式筛选  6.海陆空  7,取消规则筛选;   filter_value：139，表示免费取消
#             8,确认方式筛选;   filter_value：141，立即确认
#             9,供应商类型筛选; filter_value: 138，表示艺龙直销
#             10,礼包筛选;      filter_value: 140，有礼品
#             11, 发票模式筛选  filter_value: 1, 艺龙开发票. 2, 酒店开发票,

        request.cooperation_type = []
        # request.cooperation_type.append(1)
        # request.cooperation_type.append(2)
        # request.cooperation_type.append(3)

        request.supplier_type = []
        # request.supplier_type.append(1)
        # request.supplier_type.append(2)
        # request.supplier_type.append(3)

        request.grandson = Grandson()
        # gd = Grandson()
        request.grandson.codes = []
        # request.grandson.codes.append(2000)
        # request.grandson.codes.append(2016)

        # print "grandson: ",request.grandson


        request.customer_trait = CustomerTrait()
        request.customer_trait.trait_units = []

        # 支付方式
        trait_unit = CustomerTraitUnit()
        trait_unit.code = 1
        trait_unit.values = []
        trait_unit.values.append(1)
        trait_unit.values.append(2)

        # 早餐类型
        trait_unit1 = CustomerTraitUnit()
        trait_unit1.code = 2
        trait_unit1.values = []
        trait_unit1.values.append(1)
        trait_unit1.values.append(2)

        # 供应商
        trait_unit2 = CustomerTraitUnit()
        trait_unit2.code = 3
        trait_unit2.values = []
        trait_unit2.values.append(1)
        trait_unit2.values.append(2)

        #request.customer_trait.trait_units.append(trait_unit)
        #request.customer_trait.trait_units.append(trait_unit1)
        #request.customer_trait.trait_units.append(trait_unit2)


        #  铂涛会员
        request.group_info = []
        gi = GroupInfo()
        gi.group_id = 3600
        gi.elong_level = 8
        #request.group_info.append(gi)


        #  马甲中央定价
        # request.searchFrom = 1
        request.onlymajiadebug = True
        #request.has_majia = True
        #request.has_zydj = True
        #request.majia_zydj_switch = 31


        #  价格筛选，1：对酒店 2：对产品
        #request.select_price = SelectPrice();
        #request.select_price.type = 1;
        #request.select_price.request_price_range = []
        #price_range = RequestPriceRange();
        #price_range.low_price = 100;
        #price_range.high_price = 200;
        #request.select_price.request_price_range.append(price_range);

        # 支付方式，产品类型,供应商
        # request.settlement_type = 0;


        request.online_search_type = []

        #request.product_type = 21

        # 促销
        request.order_from_id = 50
        request.proxy_id = 'ZD'  # 'AB114'
        request.promotion_channel_code = '1041'
        request.request_origin = 3

        # 五折
        #request.half_discount_promotion = True
        #request.discount_method = 3
        #request.return_has_discount_promotion_hotel = True
        #request.return_discount_hotel = 3

        # 促销黑名单
        #request.promotion_black_list = PromotionBlackList()

        # 铂涛
        #request.botao_customer_level = 1
        request.use_botao_promotion = True
        request.use_day_promotion = True


        # FilterCondition
        request.filter_conditions = []
        fc = FilterCondition()
        fc.type,fc.apply_level,fc.use_or_not = 17,2,1
        request.filter_conditions.append(fc)

        # 酒店+产品 过滤
        request.return_noinv_or_noprice_product = True
        #request.return_has_coupon_hotel = False
        #request.return_has_no_danbao_hotel = False

        #request.return_assemble_product = []
        #request.return_assemble_product.append(1)


        # top2排序
        #request.list_product_info = ListProductInfo()
        #request.list_product_info.return_min_price_product = True
        #request.list_product_info.need_sorted_top_product = True
        #request.list_product_info.top_product_num = 2
        #request.list_product_info.sort_types = 1
        #request.list_product_info.return_min_stay_product = True

        # 返回特定产品   景酒打包
        request.return_hotel_ticket_product = True
        return request


def handle(req,res):

    result = ShowDSResult(res,req)
    result.showNormal()
    # print "\033[35m----------------\033[0m"
    # result.showDebugInfo()

    # result.Product()


    # print "+++++++++++++++++++++++++++++++"
    # count = 0
    # for detail in res.hotels_detail:
    #
    #     print "mhotel_id: ",detail.mhotel_id
    #     print "product_count: ",detail.product_count
    #     print "product_can_be_showed: ",detail.product_can_be_showed
    #     if detail.product_count == 0 and detail.product_can_be_showed == 0:
    #         print detail.mhotel_id,"被过滤"
    #         break
    #     for room in detail.room_types:
    #         for product in room.products:
    #             count = count +1
    #             rp  =product.rateplan
    #             print "count = ",++count
    #             print "mroom_name : ",room.mroom_name
    #             print "majia_id :",product.majia_id
    #             print "mroom_id : ",room.mroomtype_id
    #             print "sroomtype_id :",product.sroomtype_id
    #             print "rp_id : ",rp.rateplan_id
    #             print "supplier_id: ",product.supplier_id
    #             print "shotel_id :",product.shotel_id
    #             print "supplier_tyep: ",product.supplier_type
    #             print "cooperate_type: ",product.cooperation_type
    #             print "is_resale_product :",product.is_resale_product
    #             print "order_id :",product.order_id
    #             print "weight: ",product.weight
    #             print "===  room_num_status : %s  ===",product.room_num_status
    #             print "===================================="
    #
    #
    #             prices =  product.price
    #             print "price_status_all :",prices.price_status
    #             print "=======  price  ======="
    #             for price in prices.day_prices:
    #                 print "date: ",price.date
    #                 print "status: ",price.status
    #                 print "currency: ",price.currency
    #                 print "gen_sale_cost_origin: ",price.gen_sale_cost_origin
    #                 print "gen_sale_price: ",price.gen_sale_price
    #                 print "sale_price_with_drr: ",price.sale_price_with_drr
    #                 print "sale_price_with_drr_origin: ",price.sale_price_with_drr_origin
    #                 print "sale_price_with_drr_sub_coupon: ",price.sale_price_with_drr_sub_coupon
    #                 print "================="


def main(id,ci,co,type):

        req = build_message(id,ci,co,type)
        socket = TSocket.TSocket(HOST,PORT)
        transport = TTransport.TFramedTransport(socket)
        protocol = TCompactProtocol.TCompactProtocol(transport)
        client = Client(protocol)

        transport.open()
        res = client.searchProducts(req)
        handle(req.traceId,res)


if __name__ == '__main__':
    # id = int(sys.argv[1])
    # ci = int(sys.argv[2])
    # co = int(sys.argv[3])
    # main(id,ci,co)
    main(90000064,1,2)
