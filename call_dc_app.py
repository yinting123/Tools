#!/usr/bin/env python
#-*- coding: utf-8 -*-

from google.protobuf import text_format
import logging
import struct
import socket
import sys
import time
import traceback
import datetime
from ShowResult import  *

import productsearch_if_pb2
#import common_types_pb2

#HOST = '192.168.14.144'
#PORT = 3050
#HOST = '192.168.17.43'
#PORT = 5050
#HOST = '10.35.15.128'
#PORT = 5050
#HOST = '192.168.76.43' 
#HOST = '192.168.110.100' 
HOST = '192.168.78.43'
#HOST = '192.168.64.43'
# HOST = '192.168.14.145'
#HOST = '192.168.233.17'
#HOST = '192.168.79.43'
#PORT = 5750
PORT = 5100
CI = 0
CO = 1


def build_message(nshead,id,ci,co):
    global  request
    request = productsearch_if_pb2.SearchRequest()
    #request.mhotel_ids.append(id)
    #request.booking_datetime = 1442667600#1429758000 - 3601
    global CI
    CI = int(ci)
    CO = int(co)
    request.checkin_date = int(time.time()) + 86400*CI
    request.checkout_date = int(time.time()) + 86400*CO
    mroomattr1 = request.mhotel_attrs.add()
    mroomattr1.mhotel_id = id
    #小时房
    fc = request.filter_conditions.add()
    # fc.type = 13
    # fc.apply_level = 2
    print "filterCondition:\n %s"%fc

    request.judge_only_has_product = True

    request.request_origin = 1
    request.return_noinv_or_noprice_product=True
    #request.only_consider_salable = False

    #发票类型
    fc = request.filter_conditions.add()
    # fc.type = 11
    # fc.use_or_not = 1
    # ##fc.filter_value = 2
    # fc.filter_value = 2
    # fc.apply_level = 1
    print "====================="
    print "filterCondition\n %s"%fc
    # if fc.type == 11 :
    #    #if fc.filter_value == 1 :
    #       #if fc.apply_level == 1:
    #           #print "产品过滤，艺龙开发票"
    #       #if fc.apply_level == 2:
    #           #print "酒店过滤，艺龙开发票"
    #   #elif fc.filter_value == 2:
    #       #if fc.apply_level == 1:
    #           #print "产品过滤，酒店开发票"
    #       #if fc.apply_level == 2:
    #           #print "酒店过滤，酒店开发票"
    # print "====================="
    #直签
    #request.supplier_type.append(1)
    #request.supplier_type.append(2)
    #request.supplier_type.append(3)
    #request.cooperation_type.append(0)
    #request.cooperation_type.append(1)
    #request.cooperation_type.append(2)
    #request.cooperation_type.append()
    #print "supplier_type: %s\n cooperation_type: %s\n"%(request.supplier_type,request.cooperation_type)

    #发票
    #fc = request.filter_conditions.add()
    #fc.type = 9
    #fc.apply_level = 1
    #fc.filter_value = 138
    #fc.filter_value = 2
    #print "filterCondition: \n%s "%fc
    #print "filterCondition: \n%s "%request.filter_conditions
    
    #只考虑可售
    #request.only_consider_salable = True
    #print "request.consider_salable: ",request.only_consider_salable

	#	铂涛会员    	  #
    global gri,cl
    #gri = None
    #gri = request.group_info.add()
    #gri.group_id = 3600
    ##gri.elong_level = 1039
    #gri.elong_level = level
	#print "group_info in request is :",gri
	#if gri != None:
	    #cl = gri.elong_level
	#else:
	    #cl =1039

	#	海陆空过滤	   #	
	#   产品类型+供应商 	   #
	#fc = request.filter_conditions.add()
	#fc.type = 6
	#fc.use_or_not = 1
	#fc.apply_level = 1
	#fc.filter_value = 3 	    #8192  #16384    #2^14
	##fc.exclude_value_array.append(187577)
	#fc.exclude_value_array.append(21771)
	#fc.partial_match = False
       ####	productTypeBlackList	###
	#ptb = fc.ptb_array.add()
	#ptb.product_type = 3
	#ptb.supplier_ids.append(187577)
	#ptb.supplier_ids.append(21771)
	#ptb.partial_match = False

	#print "filtercondition:\n===================== \n",request.filter_conditions
	#print "========================\nfiltercondition: \n%s \n===================== \n"%fc


	#	产品过滤 0.今日特价 1.五折	2.限时抢  3.周边特价   #
#	request.return_assemble_product.append(0)
#	request.return_assemble_product.append(1)
#	request.return_assemble_product.append(2)
#	request.return_assemble_product.append(3)

	
#	##	用户特征与打分策略	##
#    grandson = request.grandson
#    grandson.codes.append(2031)
#    print "grandson :\n",request.grandson
#    
#    ctr = request.customer_trait
#	##	======现付
#    ctr_unit1 = ctr.trait_units.add()
#    ctr_unit1.code = 1 
#    ctr_unit1.values.append(0)
#    ctr_unit1.values.append(1)
#    #ctr_unit1.values.append(0)
#
#	##	=====早餐
#    ctr_unit = ctr.trait_units.add()
#    ctr_unit.code = 2
#	#ctr_unit.values.append(3)
#	#ctr_unit.values.append(1)
#	#ctr_unit.values.append(2)
#    ctr_unit.values.append(0)
#
#	##	=======供应商
#    unit = ctr.trait_units.add()
#    unit.code = 3
#    unit.values.append(2)
#    unit.values.append(1)
#    print "customer_trait :\n",request.customer_trait
#    print "==========="
#    units = request.customer_trait.trait_units
#    for unit in units:
#        #length = len(unit.values)
#        #print "len is :",length
#        if unit.code ==1 and unit.values[len(unit.values)-1]==1 and (request.grandson.codes[0] & 1 !=0):
#            print "现付"
#        if unit.code==2:
#            for value in unit.values:
#                if value == 0 and (request.grandson.codes[0] & 2 !=0):
#                    print "无早"
#                    break
#        if unit.code==3 and unit.values[len(unit.values)-1]==1 and (request.grandson.codes[0] & 4 !=0):
#            print "艺龙"
#    if request.grandson.codes[0] & 8 !=0:
#        print "立即确认"
#    print "============="
        
##	data={'1':()}
#

	##  促销
    request.proxy_id =  'ZD'  #'AB114' #'ZD'
    request.promotion_channel_code = '1041'
    request.order_from_id = 50
    request.discount_method = 3
    #request.half_discount_promotion = True
    request.use_day_promotion = True
    #request.product_type = 32 	
    ##	request.min_price_excluded_products = 32
    #	print "min_price_excluded",request.min_price_excluded_products
    #	print "product_type:",request.product_type
    #request.booking_channel = 4
    #request.sell_channel = 2
    #	request.product_type = 0
    ###================================
	##=================================

    #最低价不计算
#	request.min_price_excluded_products = 9
#	request.order_from_id = 50

	#request.online_search_type.append(1)
	#selectprice1 = request.select_price
    	#selectprice1.type=1
    	#request_price_range1 = selectprice1.request_price_range.add()
    	#request_price_range1.low_price=200
    	#request_price_range1.high_price=300
	
	#top2sort = request.list_product_info
    	#top2sort.return_min_price_product=True
    	#top2sort.need_sorted_top_product=True
    	#top2sort.top_product_num=100
    	#top2sort.sort_types=1
	#top2sort.return_min_stay_product = True
	
	#checkin1 = request.checkin_person_for_oneroom 
	#checkin1.min_checkin_person_for_oneroom = 100
	
	#half_discount
#	request.half_discount_promotion = True
	#request.return_has_discount_promotion_hotel = True
	#request.return_discount_hotel = 1 
	#request.min_price_calc_with_halfdiscount_pro=3

	#request.botao_customer_level =True
	#request.use_botao_promotion =True
    #request.onlydebg = True
	#request.return_longcuionly_hotel=True
    	#request.search_method = 4
    #print "return_noinv_or_noprice_product: ",request.return_noinv_or_noprice_product
#	request.price_sub_coupon = True
	#request.return_freesale_msg = True
	#request.return_has_allbuyroom_hotel = True	
	#request.return_has_manjian_hotel = True	
    	#request.language = 1
	#mroomattr1 = request.mhotel_attrs.add()
	#mroomattr1.mhotel_id = id
	#mroomattr1 = request.mhotel_attrs.add()
#	mroomattr1.mhotel_id = 40101570
#	request.return_assemble_product.append(1)
#	request.return_assemble_product.append(2)
#	request.return_assemble_product.append(3)
#	request.return_assemble_product.append(0)
#	request.min_price_excluded_products = 8


#	排序 sort2
#	list_product_info = request.list_product_info
#	list_product_info.return_min_price_product = True
#	list_product_info.need_sorted_top_product = True
#	list_product_info.return_min_price_product = True
#	list_product_info.top_product_num = 2
#	list_product_info.sort_types = 1
#
	
	#mroomattr1.mroom_filter = True
	#mroomattr1.selected_mroom_ids.append(1023)
	###	列表页code
	#codes = (43,1,2,3,4,5,6,7,8,9,10,11,28,33,34,35,36,37,38,40,41,42)
#	###	详情页code
#	codes = (43,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)
#	###	所有的code
    codes = (1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,46)
    #codes = (1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43)
    #codes = (1,2,3,4,5,6,7,8,9,10,12,13,16,17,18,21,22,25,26,27,28,31,32)
    #	print codes
    for i in codes:
        request.codes.append(i)
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(request.checkin_date))
    print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(request.checkout_date))
    #print time.strftime('%Y-%m-%d %H:%M:%S',time(request.booking_datetime))
    #print request
    return request.SerializeToString(), request.ByteSize()
   
    #print request.checkin_date
    #print request.checkout_date


def handle_response(serialized_msg):
    response = productsearch_if_pb2.SearchResponse()
    response.ParseFromString(serialized_msg)
    #print response
    # text_format.PrintMessage(response, sys.stdout,as_utf8=True,as_one_line=False)
    showResult = ShowResult(request,response)
    showResult.Product()



def main(id,ci,co):
    print "come to main"
    nshead = struct.Struct("HHI16sIII");
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    try:
        # connect
        #s.connect((HOST, PORT))
        # send
        #for p in range(10000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if id%2==0:
            #PORT=8080
            #PORT=5750
            PORT=5750
            # HOST='10.35.15.130'
            print "host :%s port :%s"%(HOST,PORT)
        else:
            # HOST='10.35.15.131'
            PORT=5751
            # PORT=port
            print "host :%s port :%s"%(HOST,PORT)
        #print "port :",PORT
	s.connect((HOST, PORT))
        msg,length = build_message(nshead,id,ci,co)
        head = nshead.pack(1,1,1,"abc",1,0,length)
        a = datetime.datetime.now()
	s.sendall(head)
        s.sendall(msg)
        time.sleep(2)
            # receive
        data = s.recv(nshead.size)
        b = datetime.datetime.now()
            #print b-a
        if len(data) == nshead.size:
                head_id, version, log_id, provider, magic, method_id, body_len = \
                    nshead.unpack(data)
                if body_len != 0:
                   serialized_msg = s.recv(body_len)
                   b = datetime.datetime.now()
                   handle_response(serialized_msg)
                else:
                    print "Received an empty message"
        else:
            logging.warning("Receive bad nshead header, length=%d", len(data))
        s.close()
            #time.sleep(5)


    except socket.error, e:
        logging.warning(e)
        traceback.print_exc()
    finally:
        s.close()
    
#main(int(90000064),1,2)

if __name__ == '__main__':
    try:
	global ci,level,port
        id = sys.argv[1]
        ci = sys.argv[2]
        co = sys.argv[3]

	#count = 0
	#for count in range(0,1000):
        main(id,ci,co)
	# main(101338,0,1)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(e)
        raise
