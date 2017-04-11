#-*-coding:utf-8-*-
__author__ = 'ting.yin'

from gen.cm.ttypes import *
import re,time
from datetime import datetime as dt

derivative_type = [0,1,2,3,4,5,6,7,811,812,813,814]

# 找指定产品
def SearchProduct(res,shotel_id,room_id,rp_id,derivative_type):
    for detail in res.hotels_details:
        for room in detail.room_types:
            for product in room.products:
                if shotel_id == product.shotel_id and\
                    room_id == product.sroomtype_id and\
                    rp_id == product.rateplan.rateplan_id and\
                    derivative_type == product.derivative_type:
                    return product

    return None


# start  到店时间
def hasAddition(product,id):
    """
    @param      product、id
    @return:    返回产品的addition值
    """
    rp = product.rateplan
    for adt in rp.additions:
        if adt.addition_id == id :
            if adt.addition_id  == 11:
                return adt.addition_value_str
            else:
                return adt.addition_value
    return None

#到店时间过滤，三种过滤情况
def Filter_ArriveTime(str,req_time,check_in):
    """
        @param  addition时间，bookingdate，check_in，check_out
        @desc
            过来情况
            1.当天订前天，不跨天的过滤
            2.当天订前天，跨天，endtime <= booking_time 过滤
            3.今天定今天，不跨天，endtime <= booking_time 过滤
        @return
            返回True，不屏蔽
            返回False，被屏蔽
    """
    h1 = re.split('-|:',str)[0]
    m1 = re.split('-|:',str)[1]
    hour = re.split('-|:',str)[2]
    min = re.split('-|:',str)[3]
    dd = dt.fromtimestamp(req_time)
    # 预定日期
    check_in = int(time.mktime(dt.fromtimestamp(check_in).date().timetuple()))
    h = dd.hour
    m = dd.minute
    s = dd.second
    # 预定日期
    booking_date = int(time.mktime(dd.date().timetuple()))
    # 预定时间
    booking_time = h * 3600 + m *60 + s
    start_time = int(h1) * 3600 + int(m1) * 60
    end_time = int(hour) * 3600 + int(min)*60

    if booking_time % 3600 == 0:
        pass
    else:
        booking_time = (booking_time/3600 + 1)*3600

    print booking_date,check_in
    """
        今天定昨天
    """
    if (booking_date > check_in) and (start_time < end_time):
        return False
    elif (booking_date > check_in) and (start_time > end_time) and (booking_time >= end_time):
        return False
    # 今天定今天
    elif ((booking_date == check_in) and (start_time < end_time) and (booking_time >= end_time)):
        return False
    else:
        return True

# True:pass  False：过滤
#酒店所有产品是否都满足到店时间过滤
def Filter_Arrive_Time(res,booking_time,ci):
    """
        @desc
            所有产品都符合True，有不符合的False
        @param
            res、booking_time、ci:
        @return
            有被过滤，False；所有都符合，True
    """
    found = False
    count = 0
    for detail in res.hotels_details:
        for room in detail.room_types:
            for product in room.products:
                addition = hasAddition(product,11)
                if addition is None:
                    count += 1
                    print '没有addition=11'
                    pass
                else:
                    print 'addition:',addition
                    # print 'booking_time:',booking_time
                    # false，被过滤
                    flag = Filter_ArriveTime(addition,booking_time,ci)
                    print 'addition:',addition
                    if not flag:
                        found = True
                        break
        if found:
            break
    if (found or count == 0):
        return False
    else:
        return True

# 预定时间 >= 结束时间
def BookingTime_Ge_EndTime(booking_time,str):
    """
        @param
            booking_time、str
        @desc
            预定时间大于结束时间
            1.大于等于，返回True
            2.False，小于
        @return
    """
    hour = re.split(':|-',str)[2]
    min = re.split(':|-',str)[3]
    end_time = int(hour) *3600 + int(min)*60

    dd = dt.fromtimestamp(booking_time)
    hour1 = dd.hour
    min1 = dd.minute
    sec = dd.second
    booking_time = int(hour1)*3600 + int(min1)* 60 + int(sec)

    if booking_time % 3600 == 0:
        pass
    else:
        booking_time  = (booking_time/3600 + 1)*3600
    if booking_time >= end_time:
        print booking_time,end_time
        return True

# 找到预定时间大于结束时间的产品
def Should_Be_Filted_By_ArriveTime(res,booking_time):
    """
    :param res、booking_time
    :return:  返回有addition=11，并且预定时间大于结束时间的产品
    """
    for detail in res.hotels_details:
        for room in detail.room_types:
            for product in room.products:
                addition = hasAddition(product,11)
                if addition is not None:
                    flag = BookingTime_Ge_EndTime(booking_time,addition)
                    if flag:
                        print '请求2、3，找到应该被arriveTime过滤的产品'
                        # print product
                        print addition
                        return product
    return None

# 找特定的标签
def Has_Flag(res,id):
    """
    @desc
        找特定的标，找到True，否则False
    @para
        res、id
    @return
    """
    for detail in res.hotels_details:
        for flag in detail.hotel_flag:
            if flag.flag_type == id and flag.effective:
                return True
        return False

# 信用住、闪住
def isLiveProduct(product):
    return


def hasLiveProduct():
    return ;

#end 闪住信用住

