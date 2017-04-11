#!/usr/bin/env python
#-*-coding:utf8-*-
class ShowResult:

    result = ''
    req = ''

    def __init__(self,req,response):
        print "come to init"
        self.result = response
        self.req = req
        # print self.result

    def Product(self):
        count = 0
        print "come to product"
        for detail in self.result.hotels_detail:
            print "mhotel_id :",detail.mhotel_id
            print "product_count :",detail.product_count
            print "product_can_be_showed :",detail.product_can_be_showed
            # if self.req.use_day_promotion :
            #     if self.result.hotels_detail[0].hotel_flag :
            #         for hotel_flag in self.result.hotels_detail[0].hotel_flag:
            #             if hotel_flag.flag_type == 4 and  hotel_flag.effective:
            #                 print "尾房：true"
            # elif self.result.weifang_info:
            #     print "weifang_info :",self.result.weifang_info

            print "====================================="
            for room in detail.room_types:

                for product in room.products:
                    count += 1
                    print "count = ",count
                    print "mroomtype_id :" ,room.mroomtype_id
                    print "mroom_name :",room.mroom_name

                    rp = product.rateplan
                    settlement = rp.settlement_type
                    print "shotel_id :",product.shotel_id
                    print "sroom_id :",product.sroomtype_id
                    print "rp_id :",rp.rateplan_id
                    print "rp_name :",rp.rateplan_name_cn
                    print "suppiler_type :",product.supplier_type
                    print "cooperation_type :",product.cooperation_type
                    print "product_type :",rp.product_type
                    self.IsMaJia(product)
                    self.resaleRoom(product)
                    # self.IsHourTimeRoom(rp)
                    # print "is_limit_time_sale :",rp.is_limit_time_sale
                    # print "start_time :",rp.start_time
                    print "==================================="

    def IsHourTimeRoom(self,rp):
        if  rp.product_type & 32:
            print "钟点房：是"
        else:
            print "钟点房：否"
            print "尾房 :",rp.is_limit_time_sale
            print "======================================"

    def IsMaJia(self,product):
        print "has_majia :",product.is_majia
        print "majia_id :",product.majia_id

    def Addition(self,rp):
        for addition in rp.addtions:
            print "id :"
            print "value :"

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

    def  hotelFlag(self):
            #打标
        print "*******hotel_flag*******"
        if self.result.hotels_detail[0].hotel_flag:
            for hotel_flag in self.result.hotels_detail[0].hotels_detail :

                if hotel_flag.effective == True:
                    type = hotel_flag.flag_type
                    if type == 1 or type ==2:
                        print "铂涛红包"
                    if type == 14:
                        print "会员优惠"
                    if type == 15:
                        print "折扣率"
                    if type == 16:
                        print "最低价最多可省"
                    if type == 17:
                        print "铂涛会员价"
                    if type ==18:
                        print "活动打标"
                        print "length = ",len(hotel_flag.activity_tags)
                    print hotel_flag

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



#    for i in range(len(self.result.hotels_detail[0].room_types)):
#	#print "mroomtype_id :" ,self.result.hotels_detail[0].room_types[i].mroomtype_id
#	#print "mroom_name :",   self.result.hotels_detail[0].room_types[i].mroom_name
#	for j in range(len(self.result.hotels_detail[0].room_types[i].products)):
#	    ##	产品，rp
#	    products = self.result.hotels_detail[0].room_types[i].products[j]
#	    shotel_id = products.shotel_id
#	    rp = products.rateplan
#	    settlement = rp.settlement_type
#	    count += 1
#            print "count = ",count
#	    ##	shotel_id	rp_id	支付方式    供应商  早餐
#	    print "shotel_id: ",products.shotel_id
#            print "supplier_id:" ,products.supplier_id
#	    ouppilier = products.supplier_name
#            print "sroomtype_id: ",products.sroomtype_id
#	    print "rp_id: ",rp.rateplan_id
#	    realType = rp.product_type & 64
#	    print "product_type: ",rp.product_type
#	    print "real_type: ",realType
#	    if settlement ==1 and realType == 0:
#		print "现付：true"
#	    else:
#		print "现付：false"
#
#            print "process_time:",products.supplier_confirm_avg_time
#	    ciDate = time.strftime("%Y.%m.%d",time.localtime(time.time()+CI*86400))
#	    ###	    早餐（ addvalue + special ）
#	    for l in range(len(rp.add_breakfast_info_of_days)):
#		special_breakfast = rp.add_breakfast_info_of_days[l]
#		#print "*********    specialBreakfast   *********"
#		#print "is_included :",special_breakfast.is_include
#		#print "share :",special_breakfast.share
#		#print "date  :",special_breakfast.date
#		special = rp.add_breakfast_info_of_days[0]
#		if special != None:
#		    date = special.date
#		    share = special.share
#		    if date == ciDate:
#			breakfast = share
#			#print "breakfast in special:",breakfast
#			#print "特殊早餐份额为：",share
#		    else:
#                        break
#			#print "特殊早餐份数为0"
#		    #print "*************************"
#                    #break
#
#	    for k in range(len(rp.add_value_infos)):
#		#print "*********    addvalue   *********"
#		addvalue = rp.add_value_infos[k]
#		#print "add_value_cn_name :",addvalue.add_value_cn_name
#		#print "is_include :",addvalue.is_include
#		#print "share :",addvalue.share
#		#print "is_forbidden :",addvalue.is_forbidden
#		addInfo = self.result.hotels_detail[0].room_types[i].products[j].rateplan.add_value_infos[k]
#		#print "addInfo.business_code: ",addInfo.business_code,"addInfo.is_include",addInfo.is_include
#		if (addInfo.business_code == '01') and (addInfo.is_include) == 1:
#		    if breakfast == 0:
#			breakfast = addInfo.share
#		    #print "addvalue早餐份数为：",addInfo.share
#		else :
#		    #print "addvalue早餐份数为: 0"
#		#print "*************************"
#                        break
#
#	    print "breakfast = ",breakfast
#
#
#            print "立即确认：",products.is_freesale
#            if products.supplier_type ==1 or products.supplier_type ==3:
#                print "是否艺龙：是"
#            else:
#                print "是否艺龙：否"
#
#	    breakfast = 0
#	    print "weight :",products.weight
#	    print "cvr :",products.cvr
#	    print "======================================================"
##

