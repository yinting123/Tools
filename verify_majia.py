__author__ = 'user'
#-*-coding:utf8 -*-
#!/usr/bin/env python

import re


def verify_majia(res):

    flag,msg = check_cash_majia(res)
    if flag == 1:
        print "找到现付马甲"
    else:
        print msg
    flag,msg = check_prepay_majia(res)
    if flag == 1:
        print "找到预付马甲"
    else:
        print msg


# 现付产品  91778844,0003,5559779

def check_cash_majia(res):
    shotel_id = 91778844
    room_id = 3
    rp_id = 5559779
    key = 547
    msg = ""
    flag = 0  # 1：找到  0：未找到
    for detail  in res.hotels_details:
        for room in detail.room_types:
            for product in room.products:

                if product.sroomtype_id == room_id and product.shotel_id == shotel_id:
                    rp = product.rateplan

                    if rp.rateplan_id == rp_id:
                        if product.is_majia != True:
                            pass   ##此处为原产品
                            # msg = "该产品应该是马甲，结果现在不是"
                            # return False,msg
                        else:
                            majia_id = re.split('_',product.majia_id)[2]
                            print "majia_id : ",majia_id
                            supplier_name = product.supplier_name

                            if int(majia_id) != key:
                                msg =  "该马甲对应的策略错误"
                                return False,msg
                            elif supplier_name != "住哪":
                                msg =  "马甲供应商名称错误"
                                return False,msg

                            else:
                                for promotion in product.day_marketing_promotions :

                                    for dp in promotion.day_marketing_promotion:
                                        if dp.promotion_type == 1 and  (dp.id == 6 or dp.id == 76) and  dp.upper_limit == 30.0:
                                            flag = 1
                                            break;
                                        else:
                                            pass
                                    if  flag :
                                        break
                                if not flag:
                                    msg =  "现付马甲 促销类型或者金额不对"
                                    return False,msg

                                else:
                                    price =  product.price
                                    for d_price in price.day_prices:
                                        if d_price.status == 1 and\
                                            d_price.currency == 'RMB' and\
                                            d_price.gen_sale_cost_origin == 140.0 and\
                                            d_price.gen_sale_price == 236.0 and\
                                            d_price.general_price_origin == 236.0 and\
                                                \
                                            d_price.weekend_sale_cost_origin == 140.0 and\
                                            d_price.weekend_sale_price == 236.0 and\
                                            d_price.weekend_price_origin == 236.0 and\
                                                \
                                            d_price.real_cost_origin == 140.0 and\
                                            d_price.sale_cost_origin == 140.0  and\
                                            d_price.sale_price == 236.0 and\
                                            d_price.sale_cost == 140.0  and\
                                            d_price.sale_price_with_drr == 236.0 and\
                                                \
                                            d_price.sale_price_with_drr_origin ==  236.0 and\
                                            d_price.sale_price_with_drr_sub_coupon == 206.0:

                                            msg =  "马甲测试酒店,现付马甲，马甲策略、促销、金额正确"
                                            return True,msg


                    else: ## end  rp
                        pass;
                else:
                    pass;
            ## end mroom
        ## end all
        if flag != 1:
            msg = "没找到预置的现付马甲产品"
            return False,msg

def check_prepay_majia(res):
    shotel_id = 91778844
    room_id = 1
    rp_id = 5559774
    key = 547
    flag = 0
    for detail  in res.hotels_details:
        for room in detail.room_types:
            for product in room.products:
                if product.sroomtype_id == room_id and product.shotel_id == shotel_id:
                    rp = product.rateplan
                    if rp.rateplan_id == rp_id:  ## 找到了对应的产品
                        if product.is_majia != True:
                            msg = "该产品应该是马甲，结果现在不是"
                            return False,msg
                        else:
                            majia_id = re.split('_',product.majia_id)[2]
                            supplier_name = product.supplier_name
                            if int(majia_id) != key:
                                msg =  "该马甲对应的策略错误"
                                return False,msg
                            elif supplier_name != "住哪":
                                msg =  "马甲供应商名称错误"
                                return False,msg

                            else:
                                price =  product.price
                                for d_price in price.day_prices:
                                    if d_price.status == 1 and\
                                        d_price.currency == 'HKD' and\
                                        d_price.gen_sale_cost_origin == 200.0 and\
                                        d_price.gen_sale_price == 121.66 and\
                                        d_price.general_price_origin == 322.0 and\
                                            \
                                        d_price.weekend_sale_cost_origin == 200.0 and\
                                        d_price.weekend_sale_price == 121.66 and\
                                        d_price.weekend_price_origin == 322.0 and\
                                           \
                                        d_price.real_cost_origin == 200.0 and\
                                        d_price.sale_cost_origin == 200.0  and\
                                        d_price.sale_price == 121.66 and\
                                        d_price.sale_cost == 200.0  and\
                                        d_price.sale_price_with_drr == 121.66 and\
                                            \
                                        d_price.sale_price_with_drr_origin ==  141.59 and\
                                        d_price.sale_price_with_drr_sub_coupon == 121.66:

                                        msg =  "马甲测试酒店，马甲策略、促销、金额正确"
                                        return True,msg
                    else:
                        pass
                else:
                    pass
        if flag != 1:
            msg = "没找到预置的预付马甲产品"
            return False,msg







