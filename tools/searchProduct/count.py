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
import ds_search_product

import productsearch_if_pb2
#import common_types_pb2

#HOST = '192.168.14.144'
#PORT = 3050
#HOST = '192.168.17.43'
#PORT = 5050
#HOST = '10.35.15.128'
#PORT = 5050
HOST = '192.168.76.43' 
#HOST = '192.168.78.43'
#HOST = '192.168.64.43'
#HOST = '192.168.14.145'
#HOST = '192.168.79.43'
PORT = 5750
CI = 0
CO = 1


def build_message(nshead,id):
	request = productsearch_if_pb2.SearchRequest()
        #request.mhotel_ids.append(id)
#	request.booking_datetime = 1442667600#1429758000 - 3601
        mhotel = request.mhotel_attrs.add()
        mhotel.mhotel_id = id
	CI = int(1)
	CO = int(2)
	request.checkin_date = int(time.time()) + 86400*CI
	request.checkout_date = int(time.time()) + 86400*CO
	
	###	列表页code
	#codes = (43,1,2,3,4,5,6,7,8,9,10,11,28,33,34,35,36,37,38,41,42)
#	###	详情页code
#	codes = (43,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21)
#	###	所有的code
	codes = (1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43)
	#codes = (1,2,3,4,5,6,7,8,9,10,12,13,16,17,18,21,22,25,26,27,28,31,32)
#	print codes
	for i in codes:
		request.codes.append(i)
	return request,request.SerializeToString(), request.ByteSize()
   

def handle_response(serialized_msg,id,req):
    response = productsearch_if_pb2.SearchResponse()
    response.ParseFromString(serialized_msg)
    #text_format.PrintMessage(response, sys.stdout,as_utf8=True)
    if response.hotels_detail[0]:
        if response.hotels_detail[0].product_count and response.hotels_detail[0].product_count >= 3:
            print "hotel_id :",id
            print "product_count :",response.hotels_detail[0].product_count

            #ds_search_product.CheckCtripQunarHotel(response)
#    for detail in response.hotels_detail:
#        if detail.product_count >0 :
#            print "hotel_id: %s"%detail.mhotel_id
#        for room in detail.room_types:
#            for product in room.products:
#                #count = ds_search_product.CheckProBreakfast(req,product) 
#                #if count !=0:
#                    #print "\033[35m breakfast: %s \033[0m"%count
#                #if product.supplier_confirm_avg_time > 0:
#                    #print "\033[35m avg_time: %s \033[0m "%product.supplier_confirm_avg_time
#
#                flag = ds_search_product.CheckBoTao(product);
#                if flag:
#                    print "\033[35m 该产品有铂涛产品,mhotel_id :%s\033[0m "%detail.mhotel_id;
#
def main(id):
    nshead = struct.Struct("HHI16sIII");
    #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    try:
        # connect
        #s.connect((HOST, PORT))
        # send
        #for p in range(10000):
       	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if id%2==0:
	    PORT=5750
	else:
	    PORT=5751
	s.connect((HOST, PORT))
        req,msg,length = build_message(nshead,id)
        head = nshead.pack(1,1,1,"abc",1,0,length)
        a = datetime.datetime.now()
	s.sendall(head)
        s.sendall(msg)
            # receive
        data = s.recv(nshead.size)
        b = datetime.datetime.now()
            #print b-a
        if len(data) == nshead.size:
                head_id, version, log_id, provider, magic, method_id, body_len = \
                    nshead.unpack(data)
                if body_len != 0:
                   serialized_msg=""
                   while True:
                        buf = s.recv(2048)
                        if not buf:
                            break;
                        serialized_msg += buf
                   #serialized_msg = s.recv(body_len)
                   b = datetime.datetime.now()
                   handle_response(serialized_msg,id,req)
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
    

def start(hotel_id):
    try:
        main(hotel_id)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        logging.error(e)
        raise
