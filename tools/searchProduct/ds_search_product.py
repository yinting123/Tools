#! /usr/bin/env python
#coding=utf-8
#author:yongquan.qu

import sys
import time
import os
#desc
# CheckProductCanSale(product)
# CheckProFreeCancle(req,product)
# CheckProConfirm(product)
# CheckProGift(product)
# CheckProSupplier(product)
# CheckProBreakfast(req,product)
# CheckProNnight(product)

#检查产品是否有平均确认时长
#def CheckAvgConfirmTime(product):
    #return product.supplier_confirm_avg_time >0 ? 1:0

#检查携程去哪儿酒店
def CheckCtripQunarHotel(res):
    flag = 0
    for detail in res.hotels_detail:
        for room in detail.room_types:
            for product in room.products:
                if product.supplier_id == 151330:
                    print detail.mhotel_id,'-',product.shotel_id,'携程酒店'
                    flag = 1
                    break
                elif product.supplier_id == 187569:
                    flag = 1
                    print detail.mhotel_id,'-',product.shotel_id,'Qunar酒店'
                    break
            #if flag:
                #break
        #if flag:
            #break
                    

#铂涛产品 additionId=7 ,value=9
def CheckBoTao(product):
    rp = product.rateplan
    for add in rp.additions:
       
        if add.addition_id == 7 and 3600 == add.addition_value:
            return True;
        else:
            pass;
    return False;

#检查产品是否可卖  库存和价格每天都有效
def CheckProductCanSale(product):
    return (product.room_num_status == 1 and product.price.price_status == 1)

#预付产品 settlement_type == 2 且 不是团购产品,现付产品同理
def CheckProYufu(product):
    return (product.rateplan.settlement_type == 2) and (not CheckProTuanGou(product))
def CheckProXianfu(product):
    return (product.rateplan.settlement_type == 1) and (not CheckProTuanGou(product)) 
def CheckProTuanGou(product):
    return product.rateplan.product_type >> 6 & 1

#check product is confirm
def CheckProConfirm(product):
    return product.is_freesale

#check product's gift
def CheckProGift(product):
    if len(product.gifts) > 0 :
        return True
    else:
        return False

#check supplier_type
def CheckProSupplier(product):
    if product.supplier_type == 1 or product.supplier_type == 3:
        return True
    else:
        return False


#check break_fast
def CheckProBreakfast(req,product):
    count = 0
#    for add_value in product.rateplan.add_value_infos:
#        if add_value.business_code == '01': #代码中只判断了code为01即可,没有判断add_value.is_include:
#            count = add_value.share
    for breakfast_day in product.rateplan.add_breakfast_info_of_days :
        if breakfast_day.date == time.strftime('%Y.%m.%d',time.localtime(req.checkin_date)):
            count = breakfast_day.share
    if count > 3:
        count = 3
    return count

#check 产品是否是N间起订，rp中的最少入住天数大于1即可
def CheckProNnight(product):
    if  product.rateplan.min_checkin_rooms > 1:
        return True
    else:
        return False

#统计产品是否免费取消  是：true  不是：false
#现付产品无担保规则 或者 现付产品房量担保大于1间 或者 现付产品预定当天且早于最早到店时间一小时
def CheckProFreeCancle(req,product):
    #预付产品均不是免费取消
    if not CheckProXianfu(product):
        return False

    #现付无担保产品均是免费取消
    if len(product.rateplan.vouch_infos) <= 0:
        return True

    vouch_info = product.rateplan.vouch_infos[0]
    #房量担保和最晚时间担保
    if vouch_info.is_arrive_time_vouch or vouch_info.is_room_count_vouch:
        if vouch_info.is_arrive_time_vouch:
            #预定时间大于入住时间 不可免费取消
            if req.booking_datetime > req.checkin_date:
                return False
            #预定当天时，预定时间离最晚到点时间不到一小时
            elif ((req.checkin_date - req.booking_datetime < 86400) and 
                    (time.strftime('%H:%M:%S',time.localtime(req.booking_datetime + 3600)) > vouch_info.arrive_start_time + ':00') ):
                return False
        if vouch_info.is_room_count_vouch and vouch_info.room_count <= 1:
            return False
        return True
    else: #代表是预定即需担保类型
        return False

