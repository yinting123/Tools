#-*-coding:utf-8-*-


__author__ = 'ting.yin'

import time,sys
from utils import Send,Json2Object
from utils.ds_search_product import *
from utils.Format_time import FormatTime
import multiprocessing,json
from call_sa import *
from utils.ds_search_product import *
from ShowResult import *
reload(sys)
sys.setdefaultencoding('utf-8')

# HOST = "172.21.27.25"
# HOST = "10.39.18.58"
HOST = "192.168.233.17"
# HOST = "192.168.233.2"
# HOST = "192.168.210.52"
# HOST = "192.168.233.83"
PORT = 5100

def multi_process(func,paras,num):
    pool = multiprocessing.Pool(num)
    pool.map(func,paras)
    pool.join()
    pool.close()

def build_and_send():
    ft = FormatTime()
    line = open("./data/logs_beijing").readline()
    data = json.loads(line)
    dtc = Json2Object.DictToClass()
    req = dtc.dict_to_object2(data)
    # print json.dumps(req, default=lambda o: o.__dict__)
    # return
    # req = build_message(101,0,1,1)

    page_size = 200
    req.inner_search_type = 1
    req.geo_attr.region_id = 101 #301
    req.page_rank_attr = PageRankAttribute()
    req.page_rank_attr.page_size = page_size
    req.hotel_attr.mhotel_ids = []
    req.product_attr.stay_date.check_in = ft.deltaDate(0)
    req.product_attr.stay_date.check_out = ft.deltaDate(1)
    req.customer_attr.booking_date = ft.Today()

    results = []
    for page in xrange(0,10):
        print 'page:',page
        req.page_rank_attr.page_index = page
        send = Send.SendMessage(HOST,PORT)
        res = send.process(req)
        # result = ShowResult(req, res)
        # result.statics()
        # return

        if res is not None:
            print res.total,res.count
            print res.status.msg
            if res.count > 0:
                # 统计酒店产品
                for detail in res.hotels_details:
                    results.append(detail.mhotel_id)
                    count = 0
                    if(detail.product_can_be_showed > 3 and count <= 3):
                        count += 1
                        print detail.mhotel_id
            else:
                print 'page',page,'退出'
                break
    print results



    req.inner_search_type = 4
    lenght = 0
    found = 0
    while True:
        if len(results) > 0 and len(results) > lenght and found <= 2:
            if lenght+300 > len(results):
                hotels = results[:len(results)]
            else:
                hotels = results[lenght,lenght+300]
            # print len(hotels),hotels
            lenght += 300
            req.hotel_attr.mhotel_ids = hotels
            resd = send.process(req)
            print resd.total
            if resd.total > 0:
                if productCount(resd):
                    found += 1
                #执行查找操作
                # if specialProduct(resd, [4,5,6,7]):   #特定产品
                # if productCount(resd):     #产品个数
                # if derivateProduct(resd,[4,5,6,7]):
                #     found += 1
                # if CheckCtripQunarHotel(resd):
                #     found += 1


        else:
            break

def get_one_hotel(id,ci,co):
    line = open("./data/logs_beijing").readline()
    data = json.loads(line)
    dtc = Json2Object.DictToClass()
    req = dtc.dict_to_object2(data)
    send = Send.SendMessage(HOST,PORT)
    req.inner_search_type = 4
    req.hotel_attr.mhotel_ids = []
    req.hotel_attr.mhotel_ids.append(id)
    req.customer_attr.booking_date = int(time.time())
    req.product_attr.stay_date.check_in = int(time.time()) + ci * 86400
    req.product_attr.stay_date.check_out = int(time.time()) + co * 86400
    # print json.dumps(req,default=lambda o:o.__dict__)
    res = send.process(req)
    # print res
    result = ShowResult(req,res)
    # result.statics()
    result.Product()

if __name__ == '__main__':
    build_and_send()
    # get_one_hotel(30101023,0,1)



