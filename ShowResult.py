#-*-coding:utf8-*-
#!/usr/bin/env python


import json
import sys,init
sys.path.append("./utils/")

import time
from filter import *
from cm.ttypes import *


productType = {0: "正常产品", 1: "马甲", 2: "中央定价", 3: "马甲中央定价", 4: "预付定价", 5: "预付定价马甲", 6: "预付定价中央定价",
                       7: "预付定价马甲中央定价",811: "高定高返", 812: "高定高返预付定价", 813: "高定高返中央定价", 814: "高定高返预付定价中央定价"}

settlement = {1:"现付",2:"预付"}

ip_status = {1:"有效",2:"部分有效",3:"全部无效"}

hotelFlag = {1:"botao可用",2:"",3:"",4:"",5:"担保",6:"手机专享",7:"coupon",8:"hongbao",9:"周边",
             10:"买断",11:"满减",12:"confirm",13:"最大折扣",14:"会员优惠",15:"五折",16:"N折起",
             17:"铂涛会员价",18:"活动打标",19:"钟点房",1019:"转让房",1020:"中大网视促销",
             1021:"闪住",1022:"信用住",1023:"微信专享",1024:"微信钱包新客N折",
             1025:"铂涛新会员",1026:"APP新客",1027:"景酒"}


statics = {1:"可定",2:"尾房",3:"红包",4:"周边",5:"五折",6:"买断",7:"总数",
           13:"返现",14:"限时抢",16:"闪住",17:"信用住",18:"景酒",19:"主动马甲",
           20:"被动马甲",21:"马甲数",22:""
           }
class ShowResult:

    result = ''
    req = ''

    def __init__(self,req,response):

        self.result = response
        self.req = req
        # print self.result

    def filter(self):
        print "\033[31m**\033[0m"*20
        for detail in self.result.hotels_details:
            for room in detail.room_types:
                for product in room.products:
                    flag = self.filterWeChat(product)
                    # flag = self.filterScenryHotel(product)
                    if flag :
                        print "shotel_id: ",product.shotel_id
                        print "sroom_id: ",product.sroomtype_id
                        print "rp_id: ",product.rateplan.rateplan_id

        print "\033[31m**\033[0m"*20
        # print "\033[31m**\033[0m"*10

    def filterScenryHotel(self,product):
        """
        过滤景酒打包产品
        """
        return product.is_hotel_ticket_product

    def filterCredit(self,product):
        return product.is_support_credit_live

    def filterFlash(self,product):
        return product.is_support_flash_live

    def filterWeChat(self,product):
        rp = product.rateplan
        bk = rp.booking_channel
        if bk & pow(2,10) != 0 and \
              bk & pow(2,1) ==0 and\
                bk & pow(2,4) ==0:
            return True

    def service_product(self):
        # json.d
        # print 'common_conf:\n',json.dumps((self.result.common_conf),default=lambda o:o.__dict__,indent=2)
        # print 'common_conf:\n',self.result.common_conf.wechat_for_new_user_promotion_ids
        print "status: ",self.result.status
        # self.minPrice()
        # print self.result
        # self.statics()
        count = 0
        print "\033[31m =\033[0m"*30

        # hotel_flag
        for detail in self.result.hotels_details:
            count += 1
            print "count = ",count
            print "mhotel_id :",detail.mhotel_id
            print 'product_count : ',detail.product_count
            print "product_can_be_showed: ",detail.product_can_be_showed
            # print "product_count :",detail.product_count
            # print "product_can_be_showed :",detail.product_can_be_showed
        #     # print "\n"*2
        #     # self.hotelFlag()
            # self.minPrice()

            # for room in detail.room_types:
            #     for product in room.products:
            #         rp = product.rateplan
            #         print "shotel_id :",product.shotel_id
            #         print "sroom_id :",product.sroomtype_id
            #         print "rp_id :",rp.rateplan_id
            #         # self.promotion(product)
            # print "\033[31m =\033[0m"*30

    def Product(self):
        # print 'common_conf:\n',self.result.common_conf.wechat_for_new_user_promotion_ids
        # print 'common_conf:\n',json.dumps(self.result.cities_common_conf[101],default=lambda o:o.__dict__)
        print '\033[35m***\033[0m'*10
        for detail in self.result.hotels_details:
            count = 0
            print "mhotel_id :",detail.mhotel_id
            print "product_count :",detail.product_count
            print "product_can_be_showed :",detail.product_can_be_showed
            print "==========================="
            print "min_price:",detail.min_price
            print "min_price_rp:",detail.min_price_rpid
            print "min_price_sroom:",detail.min_price_roomtypeid
            print "min_price_sub_coupon:",detail.min_price_sub_coupon

            print "\033[31m =\033[0m"*30
            for room in detail.room_types:
                print "mroomtype_id :", room.mroomtype_id
                print "mroom_name :", room.mroom_name
                for product in room.products:
                    # rp = product.rateplan
                    # for addition in rp.additions:
                    #     if addition.addition_id == 11:、
                    # if room.mroomtype_id == 1163 and product.rateplan.settlement_type == 1:
                    # if product.rateplan.rateplan_id == 481097 and product.sroomtype_id == 1:
                    #     and product.room_num_status != 3:
                    # if product.derivative_type == 0:
                    #     if product.rateplan.rateplan_id in (30501015,):
                    #     if room.mroomtype_id == 8:
                    # if product.shotel_id == 30501015 and \
                    #     product.sroomtype_id == 1 and \
                    #     # product.rateplan.rateplan_id == 416 :
                    # if product.derivative_type in (1,3,5,7):  #马甲
                    # if product.derivative_type in (2,3,6,7,813,814):  #中央价
                    # if product.derivative_type in (4,5,6,7):  #预付定价
                    # if product.shotel_id in [92047490]:
                            count += 1
                            print "     count = ",count
                            print "     shotel_id :",product.shotel_id
                            print "     supplier_id: ", product.supplier_id
                            print "     sroom_id:",product.sroomtype_id
                            print "     supplier_name: ", product.supplier_name
                            print "         rp_id: ",product.rateplan.rateplan_id
                            print "         支付方式: ",settlement[product.rateplan.settlement_type]
                            print "         产品类型: ",productType[product.derivative_type]
                            print "         立即确认: ", product.is_freesale, "     数量：", product.freesale_num
                            print "         景酒：", product.is_hotel_ticket_product
                            print "         门票信息：", product.hotel_ticket_product
                            print "         是否二手房: ",product.is_resale_product
                            print "         二手房原卖价: ",product.resale_product_original_price
                            print "         马甲ID: ",product.majia_id
                            self.credictProduct(product)
                            print "         inv-status: ", ip_status[product.room_num_status]
                            print "         price-status: ",ip_status[product.price.price_status]
                            print "         -----  库存  -----"
                            for inv in product.room_inventory_days:
                                print "         ", inv.date, "   ", inv.status, "   ", inv.amount, "  "
                            print "         -----  价格  -----"
                            for p in product.price.day_prices:
                                print "         ", p.date, "  ", p.sale_cost, "  ", p.sale_price, "  "
                            print "\033[31m     ===============\033[0m"
            print "============= \n  直连酒店个数 %s \n============= "%count
            self.hotelFlag()
            del count

    def minPrice(self):
        count = 0
        print "\033[35m***\033[0m"*10
        for detail in self.result.hotels_details:
            count += 1
            print 'count = ',count
            print 'mhotel_id: ',detail.mhotel_id
            print 'product_count: ',detail.product_count
            print 'product_can_be_show : ',detail.product_can_be_showed
            # 返前返后价
            print "返前信息"
            print "room_id:",detail.min_price_roomtypeid
            print "rp_id: ",detail.min_price_rpid
            print "min_price: ",detail.min_price

            print "\033[35m--\033[0m"*10

            print "返后信息"
            print "room_id: ",detail.min_price_sub_coupon_roomtypeid
            print "rp_id: ",detail.min_price_sub_coupon_rpid
            print "min_price_sub_coupon: ",detail.min_price_sub_coupon

            # print "返前库存列表:\n",detail.min_price_inventories
            # print "返后库存列表：\n",detail.min_price_sub_coupon_inventories
            print "\033[35m***\033[0m"*10
            # print '其他价格信息'
            # print '*'*10
            # ipi = detail.incidental_price_info
            # if ipi is not None:
            #     print 'can_sale_AC_origin:',ipi.min_price_cansale_sub_coupon_origin
            #     print 'can_sale_AC:',ipi.min_price_cansale_sub_coupon
            #
            #     if ipi.min_price_info is not None:
            #         for mpi in ipi.min_price_info:
            #             print 'type:',mpi.type
            #             if mpi.type == 1:
            #                 print '预付可卖产品最低价（返前价）'
            #             elif mpi.type == 2:
            #                 print '预付可卖产品最低价（返后价）'
            #             elif mpi.type == 3:
            #                 print '现付可卖产品最低价（返前价）'
            #             elif mpi.type == 4:
            #                 print '现付可卖产品最低价 (返后价)'
            #             elif mpi.type == 5:
            #                 print '钟点房可卖产品最低价 (返前价)'
            #             elif mpi.type == 6:
            #                 print '钟点房可卖产品最低价 (返后价)'
            #             print '----------------------'
            #             print 'min_price:',mpi.min_price
            #             print 'min_price_rpid:',mpi.min_price_rpid
            #             print 'min_price_sroomid:',mpi.min_price_sroomid
            #             print 'min_price_mroomid:',mpi.min_price_mroomid



        print "\033[35m***\033[0m"*10

    def credictProduct(self,product):
        print "             ========  闪住、信用住、直连、杂费   ========"
        print "             is_support_flash_live : ",product.is_support_flash_live
        print "             is_support_credit_live: ",product.is_support_credit_live
        print "             is_dc_product: ",product.is_dc_product
        print "             extras: ",product.extras
        print "             =========================================="

    def cashCommission(self,product):
        print "========  现付佣金   ========"
        print "%-15s%-18s%-30s%-25s%s"%("sign_type","cost_point","hotel_service_point",\
                "total_point","commission_value")
        print "%-15s%-18s%-30s%-25s%s"%(product.sign_type,product.cost_point,\
                product.hotel_service_point,product.total_point,product.commission_value)
        print "=="*55

    def promotionCash(self):
        for detail in self.result.hotels_details:
            # print detail
            if detail.promotion_stats is not None:
                for ps in detail.promotion_stats:
                    print 'promotionStatsType: ',ps.promotionStatsType
                    print 'min: ',ps.minPromotion
                    print 'max: ',ps.maxPromotion
                    print '---------------------'

    def CancleRule(self,rp):
        for info in rp.prepay_infos:
            if info.rule_type == 1:
                print '\033[34m         取消规则：不可取消\033[0m'
            else:
                print '\033[34m         取消规则：允许取消\033[0m'

    def price(self,product):
        """
        """
        price = product.price;
        print "         \033[31m----------   price  ----------\033[0m"
        print "         price-status: ",price.price_status;
        for d_price in price.day_prices:

            print "         date: ",d_price.date;
            print "         status: ",d_price.status;
            print "         currency: ",d_price.currency;
            print "         %-12s%-12s%-12s%-13s%-13s%-13s%-8s%-8s%-11s%-8s%-10s%-10s"\
                  %("gen_cost_o",\
                    "gen_sale_o",\
                    "gen_sale",\
                                \
                    "week_cost_o",\
                    "week_sale_o",\
                    "week_sale",\
                                \
                    "cost",\
                    "sale",\
                    "drr价_o",\
                    "drr",\
                    "返后","sub")
            print "         %-12s%-12s%-12s%-13s%-13s%-13s%-8s%-8s%-10s%-8s%-7s%-8s"\
                  %(d_price.gen_sale_cost_origin,\
                    d_price.general_price_origin,\
                    d_price.gen_sale_price,\
                                            \
                    d_price.weekend_sale_cost_origin,\
                    d_price.weekend_price_origin,\
                    d_price.weekend_sale_price,\
                                    \
                    d_price.sale_cost,\
                    d_price.sale_price,\
                    d_price.sale_price_with_drr_origin,\
                    d_price.sale_price_with_drr,\
                    d_price.sale_price_with_drr_sub_coupon,\
                    (d_price.sale_price_with_drr - d_price.sale_price_with_drr_sub_coupon ))
            print '         佣金:',d_price.sale_price_with_drr - d_price.sale_cost
            # print "general_price_origin: ",d_price.general_price_origin;
            # print "gen_sale_cost_origin: ",d_price.gen_sale_cost_origin;
            # print "gen_sale_price: ",d_price.gen_sale_price;
            #
            # print "weekend_sale_cost_origin: ",d_price.weekend_sale_cost_origin;
            # print "weekend_sale_price: ",d_price.weekend_sale_price;
            # print "weekend_price_origin: ",d_price.weekend_price_origin;
            #
            # print "sale_cost: ",d_price.sale_cost;
            # print "sale_price: ",d_price.sale_price;
            #
            # print "sale_price_with_drr: ",d_price.sale_price_with_drr;
            # print "sale_price_with_drr_origin: ",d_price.sale_price_with_drr_origin;
            # print "sale_price_with_drr_sub_coupon: ",d_price.sale_price_with_drr_sub_coupon;

            print "         \033[31m-------------------------------------\033[0m"

    def updateInvSecond(self):
        for detail in self.result.hotels_details:
            for room in detail.room_types:
                for product in room.products:
                    if product.shotel_id == 90679475 and \
                        product.sroomtype_id == 18 and \
                        product.rateplan.rateplan_id == 5415876 :
                    # 状态  日期  总量（） 超售  买断  超售数量
                        for inv in product.room_inventory_days:
                            print '%-10s%-17s\033[33m%-10s%-10s%-10s%-10s\033[0m'%(inv.status,inv.date,inv.amount,inv.is_over_booking,inv.allbuyroom_amount,inv.over_sold_limit)

    def inv(self,product):
        print "         ----------   inv  ----------"
        print "         inv-status: ",product.room_num_status
        for inv in product.room_inventory_days:
            print "         date: ",inv.date
            print "         amount: ",inv.amount
            print "         status: ",inv.status
            print "         is_over_booking: ",inv.is_over_booking
            print "         allbuyroom_amount: ",inv.allbuyroom_amount
            print "         over_sold_limit: ",inv.over_sold_limit

    def promotion(self,product):
        print "         ----------   promotion  ----------"
        for mkt in product.day_marketing_promotions:
            print "         date: ",mkt.date
            if mkt.day_marketing_promotion is not None:
                print "         type     id      uplimit     priority     has_inv     left_inv"
                for d_mkt in mkt.day_marketing_promotion:

                    print "         %-9s%-9s%-12s%-12s%-14s%-12s"%(d_mkt.promotion_type,d_mkt.id,d_mkt.upper_limit,\
                        d_mkt.priority,d_mkt.has_inv_limit,d_mkt.inv_left)

                    if  d_mkt.promotion_type == 10 or d_mkt.promotion_type == 11:
                        for desc in d_mkt.promotion_description:
                            print '         ',desc

                        print '         ',d_mkt.hongbao_records
                    # print d_mkt
            print "         -------------------------------------"

    def addvalue(self,rp):
        print "————  addvalue  ————"
        for adv in rp.add_value_infos:
            print "id: ",adv.id
            print "business_code: ",adv.business_code
            print "add_value_cn_name: ",adv.add_value_cn_name
            print "add_value_eng_name: ",adv.add_value_eng_name
            print "is_include: ",adv.is_include
            print "share: ",adv.share
            print "is_forbidden: ",adv.is_forbidden

    def booking_chnnel(self,bk):
        """
        :param bk:
        :return:
        从高到低，取商取模
        """
        len = 11
        key = {1:"线上",2:"线下",3:"积分广场",4:"手机",5:"sem特殊",\
               6:"分销商",7:"交通银行",8:"东航",9:"网站展示手机渠道",\
               10:"微信专乡",11:"华为"}
        value = []
        for i in range(0,11):
            if bk / pow(2,len - i) != 0:
                bk = (bk % pow(2,len - i))
                # value.append((key[len-i]))
                print key[len-i]
        # for i in value:
        #     print(i.decode("gbk").encode("gbk"))
        # print value
        # del value

    def hasAddition(self,rp,id):
        for addition in rp.additions:
            if addition.addition_id == id:
                print '\033[33m----  Addition  ----\033[0m'
                print 'id: ',addition.addition_id
                if id == 11:
                    print 'value: ',addition.addition_value_str
                else:
                    print 'value: ',addition.addition_value

    def ShotelBooking_Rule(self,product):
        print '\033[33m-------  shotel_booking_rule  ------- \033[0m'
        for sbr in product.shotel_booking_rules:
            print 'id:',sbr.id
            print 'shotel_id:',sbr.shotel_id
            print 'cn_desc:',sbr.cn_description
            print 'en_desc:',sbr.en_description
            print 'start_date:',sbr.start_date
            print 'end_date:',sbr.end_date
            print 'booking_date_type:',sbr.booking_date_type
            print 'booking_rule_type:',sbr.booking_rule_type
            print 'start_hour:',sbr.start_hour
            print 'end_hour:',sbr.end_hour
            print 'note2:',sbr.note2
            print 'limit1:',sbr.limit1
            print 'limit2:',sbr.limit2
        print '\033[33m-------  shotel_booking_rule  ------- \033[0m'
            # print sbr

    def shotel_invoice_info(self):
        for detail in self.result.hotels_details:
            for invoice in detail.shotel_invoice_info:
                print 'shotel_id: ',invoice.shotel_id
                print 'type: ',invoice.type
            print '\033[35m ****\033[0m'*10

    def IsHourTimeRoom(self,rp):
        if  rp.product_type & 32:
            print "钟点房：是"
        else:
            print "钟点房：否"
            print "尾房 :",rp.is_limit_time_sale
            print "======================================"

    def IsMaJia(self,product):
        print "is_majia :",product.is_majia
        print "majia_id :",product.majia_id

    def Addition(self,rp):
        print "         \033[34m ====  addition  ==== \033[0m"
        for addition in rp.additions:
            print "         id :",addition.addition_id
            if addition.addition_id != 11:
                print "         value :",addition.addition_value
            else:
                print "         str :",addition.addition_value_str
            # print "         -----------------------------------"
            print "         \033[34m======================\033[0m"

    def resaleRoom(self,product):
        print "is_resale_product: ",product.is_resale_product
        print "order_id: ",product.order_id

    def ProductRank(self):
        print "############################"
        print "#			                #"
        print "#	    产品排序	            #"
        print "#			                #"
        print "############################"

        global breakfast
        count=0
        breakfast = 0
        print "product_count: ",self.result.hotels_detail[0].product_count
        print "product_can_be_showed: ",self.result.hotels_detail[0].product_can_be_showed
        print "grandson: ",self.result.grandson
        print "============================="
        for detail in self.result.hotels_detail:
            for room in detail.room_types:
                print "mroomtype_id :" ,room.mroomtype_id
                print "mroom_name :",room.mroom_name
                for product in room.products:
                    rp = product.rateplan
                    settlement = rp.settlement_type
                    print "shotel_id :",product.shotel_id
                    print "sroom_id :",product.sroomtype_id
                    print "rp_id :",rp.rateplan_id
                    print "rp_name :",rp.rateplan_name
                    print "支付方式 :"
                    print "早餐类型 :"
                    print "是否艺龙 :"
                    print "weight :",product.weight

    def onlineSearch(self):
        print "############################"
        print "#                          #"
        print "#       直销产品            #"
        print "#                          #"
        print "############################"

        count = 0
        for detail in self.result.hotels_detail:
            print "product_count:",detail.product_count
            print "product_can_be_showed: ",detail.product_can_be_showed

            print ""
            print "====================="
            #直签非直签内容：shotel_invoice_info，rateplanAddition，supplier_type，cooperate_type
            for invoice in detail.shotel_invoice_info:
                print "SHotelInvoiceInfo \n shotel_id: %s\n type: %s "%(invoice.shotel_id,invoice.type)
                print "——————————————————"
            print "====================="
            for room in detail.room_types:
                for product in room.products:
                    count = count +1
                    hours = product.rateplan.product_type & 32
                    print "count = %s"%count
                    if hours:
                        print "小时房：是"
                    else:
                        print "小时房：否"
                    print "mroom_name: %s"%room.mroom_name
                    print "sroomtype_id: %s"%product.sroomtype_id
                    print "shotel_id: %s"%product.shotel_id
                    print "rp_id: %s"%product.rateplan.rateplan_id
                    print "customer_level :%s"%product.rateplan.customer_level
                    print "supplier_id: %s"%product.supplier_id
                    print "supplier_type: %s"%product.supplier_type
                    print "cooperation_type: %s"%product.cooperation_type
                    if 1 == product.supplier_id or 3 == product.supplier_id or 1 == product.cooperation_type:
                        print "直签：true"
                    else:
                        print "直签：false"
                    print "——————————————————"
                    for addition in product.rateplan.additions:
                        print "additions \n addition_id: %s \n addition_value: %s \n  "%(addition.addition_id,addition.addition_value)
                    print "——————————————————"
                    print "room_num_status: %s"%product.room_num_status
                    print "====================="

    def statics(self):
        # for detail in self.result.hotels_details:
        #     for flag in detail.hotel_flag:
        #         if flag.flag_type == 1028 and flag.effective:
        #             flash += 1
        #             hotels_f.append(detail.mhotel_id)
        #         if flag.flag_type == 1022 and flag.effective:
        #             credit += 1
        #             hotels_c.append(detail.mhotel_id)
        # print "景酒酒店：%s\n 闪住共:%s家"%(hotels_f,flash)
        # print "信用住酒店：%s\n 信用住共:%s家"%(hotels_c,credit)

        static = self.result.statistics
        # print static
        # print statics.keys()
        for item in static.static_count:
            if item.id in statics.keys():
                print item.id,"     ",statics[item.id],"       ",item.num

    def hotelFlag(self):
            #打标
        show = []
        dict = {}
        print "\033[35m*******hotel_flag*******\033[0m"
        print "flag_type     effective      uplimit"
        if self.result.hotels_details[0].hotel_flag:
            for hotel_flag in self.result.hotels_details[0].hotel_flag :

                if hotel_flag.effective == True:
                    show.append((hotel_flag.flag_type,hotel_flag.effective,hotel_flag.upper_limit))
                    type = hotel_flag.flag_type

                    if type == 1 or type ==2:
                        print "铂涛红包"

                    elif type == 7:
                        print "coupon"
                    elif type == 8:
                        print "红包"
                    elif type == 11:
                        print "满减"
                    elif type == 13:
                        print "最大折扣"
                    elif type == 14:
                        print "会员优惠"
                    elif type == 15:
                        print "折扣率"
                    elif type == 16:
                        print "最低价最多可省"
                    elif type == 17:
                        print "铂涛会员价"
                    elif type ==18:
                        print "活动打标"
                        print "length = ",len(hotel_flag.activity_tags)
                    # else:
                    #     print
                        # print hotel_flag
        for i in range(len(show)):
            print "%-15s%-15s%-10s"%(show[i][0],show[i][1],show[i][2])

    def DebugPromotion(self):
        for d_detail in self.result.debug_response:
            for d_shotel in d_detail.mhotel.shotel:
                for d_sroom in d_shotel.sroom:
                    for d_product in d_sroom.product:
                        for d_promotion in d_product.promotion:
                            print "debug_shotel_id :",d_product.shotel_id
                            print "debug_product_id:",d_product.product_id
                            print "debug_rp_id:",d_product.rp_id
                            print "debug_sroom_id:",d_product.sroom_id
                            print "===========  debug promotion  ==========="
                            print "date:",d_promotion.date
                            print "promotion_id:",d_promotion.promotion_id
                            print "promotion_type:",d_promotion.promotion_type
                            print "use_ok:",d_promotion.us_ok
                            print "reson:",d_promotion.reason
                            print "uplimit:",d_promotion.upperlimit
                            print "----------------"

    def hasCredit(self):
        for detail  in self.result.hotels_details:
            for flag in detail.hotel_flag:
                if flag.flag_type == 1021 or flag.flag_type == 1022:
                    print '有闪住,信用住'
            print '\033[33m ********'
        print '\033[35m***\033[0m'*10

    def DrrMsg(self,product):
        print '         \033[34m ==== drrMsg ====\033[0m  '
        drrMsg = product.drrMsg
        print '         ',drrMsg
        print '         \033[34m =================\033[0m  '

class ShowDSResult():
    def __init__(self,result,*args):
        self.res = result
        if len(args) > 0:
            self.req = args

    def showNormal(self):
        print self.req,'\n--------------------------------------'
        for detail in self.res.hotels_detail:
            print "mhotel_id:",detail.mhotel_id
            print "product_count:",detail.product_count
            print "product_can_be_showed:",detail.product_can_be_showed
            if detail.room_types is not None:
                for room in detail.room_types:
                    print "     mroom_name:", room.mroom_name
                    print "     mroom_id:",room.mroomtype_id
                    if room.products is not None:
                        for product in room.products:
                            print "         shotel_id:",product.shotel_id
                            print "         sroom_id:",product.sroomtype_id
                            print "         rp_id:",product.rateplan.rateplan_id
                            print "         rp_name:",product.rateplan.rateplan_name_cn
                            print "         supplier_id",product.supplier_id
                            print "         supplier_name",product.supplier_name
                            print "         产品类型:",productType[product.derivative_type]
                            print "         支付方式:",settlement[product.rateplan.settlement_type]
                            print "         景酒：",product.is_hotel_ticket_product
                            print "         门票信息：",product.ticket_resource_infoes
                            # print "         总库存：",product.room_num_status
                            # print "         总价格：",product.price.is_effective
                            # print "         库存"
                            print "             ----------"
                            for inv in product.room_inventory_days:
                                print "             ",inv.date,"   ",inv.status,"   ",inv.amount,"  "
                            # print "         价格"
                            print "             ----------"
                            for p in product.price.day_prices:
                                print "             ",p.date,"  ",p.sale_cost,"  ",p.sale_price,"  ",  p.sale_price_with_drr," ",p.sale_price_with_drr_sub_coupon
                            print "         ===================="
        self.hotelFlag()

    def showDebugInfo(self):
        for detail in self.res.debug_response:
            print "mhotel_id:",detail.mhotel.mhotel_id
            print "reason::",detail.mhotel.reason
            if detail.mhotel.shotel is not None:
                for shotel in detail.mhotel.shotel:
                    print "     shotel_id:",shotel.shotel_id
                    print "     is_ok:",shotel.return_ok
                    print "     reason:",shotel.reason
                    print "     supplier_id:",shotel.supplier_id
                    print "     supplier_name:",shotel.supplier_name
                    if shotel.sroom is not None:
                        for sroom in shotel.sroom:
                            print "             mroom_id:",sroom.mroom_id
                            print "             mroom_name:",sroom.mroom_name
                            print "             sroom_id:",sroom.sroom_id
                            print "             is_ok:",sroom.return_ok
                            print "             reason:",sroom.reason
                            print "             inv_type:",sroom.inventory_type
                            if sroom.product is not None:
                                for product in sroom.product:
                                    print "                 product_id:",product.product_id
                                    print "                 shotel_id:",product.shotel_id
                                    print "                 sroom_id:",product.sroom_id
                                    print "                 rp_id:",product.rp_id
                                    print "                 is_ok:",product.return_ok
                                    print "                 reason:",product.reason
                                    print "                 ======================="

    def hotelFlag(self):
        show = []
        print "\033[35m*******hotel_flag*******\033[0m"
        print "name         flag_type        effective    uplimit"
        if self.res.hotels_detail[0].hotel_flag:
            for hotel_flag in self.res.hotels_detail[0].hotel_flag :
                if hotel_flag.effective == True:
                    show.append((hotel_flag.flag_type,hotel_flag.effective,hotel_flag.upper_limit))

        for i in range(len(show)):
            print "%-15s%-15s%-15s%-10s"%(hotelFlag[show[i][0]],show[i][0],show[i][1],show[i][2])

    def ShowInvForNB(self):
        print "return_code:",self.res.return_code
        print "returna_msg:",self.res.return_msg
        # print self.res.mhotel_detail
        for detail in self.res.mhotel_detail:
            print "mhotel_id:",detail.mhotel_id
            for sd in detail.shotel_detail:
                print "     shotel_id:",sd.shotel_id
                for srd in sd.sroom_detail:
                    print "         sroom_id:",srd.sroom_id
                    for invd in srd.inv_detail:
                        # self.showSame(detail.mhotel_id,sd.shotel_id,srd.sroom_id,res)
                        print "             begin_date:",time.strftime("%Y-%m-%d",time.localtime(invd.begin_date/1000 ))
                        print "             end_date:",time.strftime("%Y-%m-%d",time.localtime(invd.end_date /1000))
                        print "             begin_time:",invd.begin_time
                        print "             end_time:",invd.end_time
                        print "             available_amount:",invd.available_amount
                        print "             available_date:",time.strftime("%Y-%m-%d",time.localtime(invd.available_date /1000 ))
                        print "             is_over_booking:",invd.is_over_booking
                        print "             status:",invd.status
                        print "             instant_confirm:",invd.instant_confirm
                        print "             ic_begin_time:",invd.ic_begin_time
                        print "             ic_end_time:",invd.ic_end_time
                        print "         \033[33m===================\033[0m"


    # def showSame(self,mhotel_id,shotel_id,sroom_id,res):
    #     for detail in res.response.hotels_details:
    #         if detail.mhotel_id == mhotel_id:
    #             for room in detail.room_types:
    #                 for product in room.products:
    #                     if product.shotel_id == shotel_id \
    #                         and product.sroom_id == sroom_id:
    #                         print "             \033[35m*************\033[0m"
    #                         for inv in product.room_inventory_days:
    #                             print "             date:",inv.date
    #                             print "             amount:",inv.amount
    #                             print "             status:",inv.status
    #                             print "             is_over_booking:",inv.is_over_booking
    #                             print "             allbuy:",inv.allbuyroom_amount
    #                             print "             \033[33m===================\033[0m"
    #                         print "             \033[35m*************\033[0m"


















