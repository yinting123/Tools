#-*-coding:utf-8-*-

import json,sys

sys.path.append("./")
sys.path.append("./gen/")

from  readLog import  *

from thrift.transport import TSocket
from se.ttypes import *
from cm.ttypes import *
# from gen.thriftproxy.ThriftProxy import Client
#from jsonpickle._samples import Thing

class DictToClass():
    #基本数据类型
    def set_record(self,cls,data):
        for k1,v1 in data.items():
            if k1 == "ip" or k1 == "channel" \
                    or k1 == "proxy_id" or k1 == "promotion_channel_code" or k1 == "language":
                # print "转换前的为：",v1
                v1 = v1.encode("utf-8")
                # print "转换后的为:",v1
            setattr(cls,k1,v1)
        return cls

    def setHotelAttr(self,data):
        hotel_attr = HotelAttribute()
        for k1,v1 in data.items():
            if k1 == "fuzzy_search_type":
                fuzzy = FuzzySearchType._NAMES_TO_VALUES
                for k2,v2 in fuzzy.items():
                    if k2 == v1:
                        v1 = v2
            elif k1 == "mroom_selected":
                select_room = []
                if v1 is not None:
                    for v in v1:
                        room_select = RoomSelected()
                        room_select = self.set_record(room_select,v)
                        select_room.append(room_select)
                    v1 = select_room

            setattr(hotel_attr,k1,v1)
        return hotel_attr

    def setProductAttr(self,data):
        product_attr = ProductAttribute()
        for k1,v1 in data.items():
            if k1 == "promotion_channel_code":
                v1 = v1.encode("utf-8")
            if k1 == "stay_date":
                stay_date = StayDate()
                v1 = self.set_record(stay_date,v1)
            if k1 == "price_pair":
                price_list = []
                for v in v1:
                    price_pair = PricePair()
                    price_pair = self.set_record(price_pair,v)
                    price_list.append(price_pair)
                v1 = price_list
            elif k1 == "list_product_info":
                list_product_info = ListProductInfo()
                v1 = self.set_record(list_product_info,v1)
            elif k1 == "promotion_black_list":
                black_list = []
                for v in v1:
                    promotion_black_list = PromotionBlackList()
                    self.set_record(promotion_black_list,v)
                    black_list.append(promotion_black_list)
                v1 = black_list
            elif k1 == "filter_conditions":
                filters = []
                for v in v1:
                    filter_conditions = FilterCondition()
                    for k2,v2 in v.items():
                        if k2 == "ptb":
                            for k3,v3 in v2.items():
                                ptb = ProductTypeBlackList()
                                v2 = setattr(ptb,k3,v3)
                        setattr(filter_conditions,k2,v2)
                    filters.append(filter_conditions)
                v1 = filters
            elif k1 == "booking_menu":
                v1 = BookingMenu._VALUES_TO_NAMES
            elif k1 == "hong_bao_records":
                hong_bao = []
                for v in v1:
                    hong_bao_records = HongbaoRecord()
                    for k2,v2 in v.items():
                        if k2 == "activity_channel":
                            channels = []
                            for v3 in v2:
                                activity_channel = ActivityChannel()
                                activity_channel = self.set_record(activity_channel,v3)
                                channels.append(activity_channel)
                            v2 = channels

                        elif k2 == "hongbao_full_back_rule":
                            full_hong_bao = HongbaoFullBackRule()
                            v2 = self.set_record(full_hong_bao,v2)
                        setattr(hong_bao_records,k2,v2)
                        hong_bao.append(hong_bao_records)
                v1 = hong_bao

            elif k1 == "order_by_user_credit_filter":
                credit_filter =  UserCreditLiveInfo()
                v1 = self.set_record(credit_filter,v1)
            setattr(product_attr,k1,v1)
        return product_attr

    def setGeoAttr(self,data):
        geo_attr = GeoAttribute()
        for k1,v1 in data.items():
            if k1 == "language":
                v1 = v1.encode("utf-8")
            if k1 == "district_type":
                district_type = DistrictType._NAMES_TO_VALUES
                for k2,v2 in district_type.items():
                    if k2 == v1:
                        v1 = v2
            elif k1 == "geo_type":
                geo_type = GeoType._NAMES_TO_VALUES
                for k2,v2 in geo_type.items():
                    if k2 == v1:
                        v1 = v2
            elif k1 == "nearby":
                nearby = NearBy()
                for k2,v2 in v1.items():
                    if k2 == "center":
                        center = Location()
                        v2 = self.set_record(center,v2)
                    setattr(nearby,k2,v2)
                v1 = nearby
            elif k1 == "bound":
                bound = Bound()
                for k2,v2 in v1.items():
                    if k2 == "left_top":
                        left_top = Location()
                        setattr(bound,k1,self.set_record(left_top,v2))
                    elif k2 == "right_bottom":
                        right_bottom = Location()
                        setattr(bound,k1,self.set_record(right_bottom,v2))
                v1 = bound
            elif k1 == "mulpoi":
                mulpoi = MulPOI()
                for k2,v2 in v1.items():
                    if k2 == "mul_pois":
                        mul_pois = NearBy()
                        for k3,v3 in v2.items():
                            if k3 == "center":
                                center = Location()
                                v3 = self.set_record(center,v3)
                            setattr(mul_pois,k3,v3)
                        v2 = mul_pois
                    setattr(mulpoi,k2,v2)
                v1 =  mulpoi
            setattr(geo_attr,k1,v1)
        return geo_attr

    def setRoomAttr(self,data):
        room_attr = RoomAttribute()
        for k1,v1 in data.items():
            if k1 == "checkin_person_for_oneroom":
                cpfo = CheckInPersonForOneRoom()
                v1 = self.set_record(cpfo,v1)
            setattr(room_attr,k1,v1)
        return room_attr

    def setCustomerAttr(self,data):
        customer_attr = CustomerAttribute()
        for k1,v1 in data.items():
            group = []
            if k1 == "group_info":
                if v1 is not None:
                    for v in v1:
                        group_info = GroupInfo()
                        group_info = self.set_record(group_info,v)
                        group.append(group_info)
                v1 = group
            if k1 == "proxy_id":
                v1 = v1.encode("utf-8")
            setattr(customer_attr,k1,v1)
        return customer_attr

    def setCallerAttr(self,data):
        caller = CallerAttribute()
        return self.set_record(caller,data)

    def setPageRankAttr(self,data):
        page_rank = PageRankAttribute()
        for k1,v1 in data.items():
            if k1 == "sort_policys":
                sort_policys = []
                for one in v1:
                    for k2,v2 in one.items():
                        sp = SortPolicy()
                        if k2 == "sort_item":
                            sort_item = SortItem._NAMES_TO_VALUES
                            # print "sort_item: \n",sort_item,'\n'
                            for k3,v3 in sort_item.items():
                                if k3 == v2:
                                    v2 = v3

                        elif k2 == "sort_item_policy":
                            sort_policy = SortItemPolicy._NAMES_TO_VALUES
                            for k3,v3 in sort_policy.items():
                                if k3 == v2:
                                    v2 = v3
                        elif k2 == "price_interval":
                            price_interval = PriceInterval()
                            v2 = self.set_record(price_interval,v2)

                        setattr(sp,k2,v2)
                    sort_policys.append(sp)
                v1 = sort_policys
            elif k1 == "sorting_method":
                sort_method  = SortingMethod._NAMES_TO_VALUES
                for k2,v2 in sort_method.items():
                    if k2 == v1:
                        v1 = v2
            elif k1 == "sorting_direction":
                sort_direct = SortingDirection._NAMES_TO_VALUES
                # print "sort_direct:\n" ,sort_direct,'\n'
                for k2,v2 in sort_direct.items():
                    if k2 == v1:
                        v1 = v2

            setattr(page_rank,k1,v1)
        return page_rank

    def setUserInfo(self,data):
        user_info = UserInfo()
        for k1,v1 in data.items():
            if k1 == "geo_info":
                geo_info = GeoInfo()
                v1 = self.set_record(geo_info,v1)
            setattr(user_info,k1,v1)
        return user_info

    def setFilterAttr(self,data):
        filter_attr = FilterAttribute()
        for k1,v1 in data.items():
            if k1 == "language":
                language = LangType._NAMES_TO_VALUES
                for k2,v2 in language.items():
                    if k2 == v1:
                        v1 = v2
            setattr(filter_attr,k1,v1)
        return filter_attr

    def setRecommendAttr(self,data):
        rec_attr = RecommendAttribute()
        return self.set_record(rec_attr,data)

    def setFastFilterAttr(self,data):
        fast_filter_attr = FastFilterAttribute()
        return self.set_record(fast_filter_attr,data)

    def setReturnAttr(self,data):
        return_attr = ReturnAttribute()
        return self.set_record(return_attr,data)
# """
#     #设置第一层
#     def set_first(self,cls,data):
#         for key,value in data.items():
#             if key == "fuzzy_search_type":
#                 value = FuzzySearchType._NAMES_TO_VALUES(value)
#             if key == "checkin_person_for_oneroom":
#                 cpfo = CheckInPersonForOneRoom()
#                 self.set_record(cpfo,value)
#                 value = cpfo
#             if key == "price_pair":
#                 price_pair = PricePair()
#
#             if key == "list_product_info":
#                 list_product_info = ListProductInfo()
#
#             if key == "promotion_black_list":
#                 promotion_black_list = PromotionBlackList()
#
#             if key == "filter_conditions":
#                 filter_conditions = FilterCondition()
#
#             if key == "booking_menu":
#                 booking_menu = BookingMenu()
#
#             if key == "hong_bao_records":
#                 hong_bao_records = HongbaoRecord()
#
#             #@cls GeoAttribute
#             #@para enum DistrictType,GeoType
#             if key == "district_type":
#                 district_type = DistrictType()
#             if key == "geo_type":
#             if key == "group_info":
#             if key == "sort_policys":
#             if key == "sorting_method":
#             if key == "sorting_direction":
# #
#             setattr(cls,key,value)
#  """
    def dict_to_object2(self,data):
        seq = tuple,list
        inner = InnerSearchRequest()
        for key,value in data.items():
            # print "key:%s\nvalue:%s\n"%(key,value)
            if key == "hotel_attr":
                hotel_attr = self.setHotelAttr(value)
                inner.hotel_attr = hotel_attr
                # print "hotel_attr:\n",hotel_attr,'\n'

            elif key == "room_attr":
                room_attr = self.setRoomAttr(value)
                inner.room_attr = room_attr
                # print "room_attr: \n",room_attr,'\n'

            elif key == "product_attr":
                product_attr = self.setProductAttr(value)
                inner.product_attr = product_attr
                # print "product_attr: \n",product_attr,'\n'

            elif key == "geo_attr":
                geo_attr = self.setGeoAttr(value)
                inner.geo_attr = geo_attr
                # print "geo_attr: \n",geo_attr,'\n'

            elif key == "customer_attr":
                customer_attr = self.setCustomerAttr(value)
                inner.customer_attr = customer_attr
                # print "customer_attr: \n",customer_attr,'\n'

            elif key == "page_rank_attr":
                page_rank_attr = self.setPageRankAttr(value)
                inner.page_rank_attr = page_rank_attr
                # print "page_rank_attr: \n",page_rank_attr,'\n'

            elif key == "caller_attr":
                caller_attr = self.setCallerAttr(value)
                inner.caller_attr = caller_attr
                # print "caller_attr: \n",caller_attr,'\n'

            elif key == "return_attr":
                return_attr = self.setReturnAttr(value)
                inner.return_attr = return_attr
                # print "return_attr: \n",return_attr,'\n'

            elif key == "user_info":
                user_info = self.setUserInfo(value)
                inner.user_info = user_info
                # print "user_info: \n",user_info,'\n'

            elif key == "filter_attr":
                filter_attr = self.setFilterAttr(value)
                inner.filter_attr = filter_attr
                # print "filter_attr: \n",filter_attr,'\n'

            elif key == "rec_attr":
                rec_attr = self.setRecommendAttr(value)
                inner.rec_attr = rec_attr

            elif key == "fastfilter_attr":
                fastfilter_attr = self.setFastFilterAttr(value)
                inner.fastfilter_attr = fastfilter_attr
                # print "fastfilter_attr: \n",fastfilter_attr,'\n'

        # print "\n\n\ninner\n",inner
            elif key == "inner_search_type":
                inner_type = InnerSearchType._NAMES_TO_VALUES
                # print "inner_type:\n",inner_type
                for k1,v1 in inner_type.items():
                    if k1 == value:
                        setattr(inner,key,v1)
            # else:
            #     setattr(inner,key,value)

        return inner
'''
    def dict_to_object3(self,inner,source):
        seq = list
        for i,j in source.items():
            if isinstance(j,dict):
            #if type(j) == dict:
                setattr(inner,i,self.dict_to_object3(j))
            elif isinstance(type(j),seq):
            #elif type(j) == list:
                # setattr(inner,i,type(j)(dict_to_object3(sj) if isinstance(type(sj),dict) else sj for sj in j))
        print inner
'''

def build(req):

    socket = TSocket.TSocket('192.168.233.17',5100)
    transport = TTransport.TFramedTransport(socket)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    # protocol = TCompactProtocol.TCompactProtocol(transport)
    client = Client(protocol)
    transport.open()
    # print "in req:\n",req
    ret = client.SearchInner(req)
    transport.close()
    handle(ret)

def handle(ret):
    print 'status:',ret.status.msg
    print 'total:',ret.total
    print 'count:',ret.count

toClass = {
    "hotel_attr":"HotelAttribute",
        "mroom_selected":"RoomSelected",
    "room_attr":"RoomAttribute",
        "checkin_person_for_oneroom":"CheckInPersonForOneRoom",
    "product_attr":"ProductAttribute",
        "stay_date":"StayDate","price_pair":"PricePair","list_product_info":"ListProductInfo",
        "promotion_black_list":"PromotionBlackList","filter_conditions":"FilterCondition",
        "hong_bao_records":"HongbaoRecord","order_by_user_credit_filter":"UserCreditLiveInfo",
    "geo_attr":"GeoAttribute",
        "district_type":"DistrictType","":"",
    "customer_attr":"CustomerAttribute",
    "page_rank_attr":"PageRankAttribute",
    "caller_attr":"CallerAttribute",
    "return_attr":"ReturnAttribute",
    "user_info":"UserInfo",
    "filter_attr":"FilterAttribute",
    "rec_attr":"RecommendAttribute",
    "fastfilter_attr":"FastFilterAttribute",

}

def toClass(key):
    if key == 'hotel_attr':
        return 'HotelAttribute'
    elif key == 'room_attr':
        return ''

def dict_to_object(req,dicts):
    for key, value in dicts.item():
        #对象
        if isinstance(value,dict):
            cla = getattr(__import__('cm.ttypes'),toClass[key])
            cls = cla()
            dict_to_object(cls,value)
        if isinstance(value,(list)):
            pass


        # 对象列表

        # 枚举

        # 正常类型
    return req


if __name__ == '__main__':
    global first
    first = 0
    filePath = "/Users/user/Documents/project/PycharmProjects/automate/searchAgent-analyse.log"
    readLogFile(filePath)
    path2 = "/Users/user/Documents/project/PycharmProjects/automate/logs"
    f = open(path2)
    line = f.readline()
    # print line
    source = json.loads(line)
    dict1 = DictToClass()
    inner = dict1.dict_to_object2(source)
    #print "inner:\n",inner
    # print type(inner)
    # build(inner)

