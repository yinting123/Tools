#-*-coding:utf-8-*-

__author__ = 'user'
from utils.Json2Object import *
from utils.readLog import *
from utils import Send
from utils.Format_time import *
from ShowResult import *
import json

# HOST = "172.21.27.25"
HOST = "10.39.18.58"
# HOST = "192.168.233.17"
# HOST = "192.168.210.52"
# HOST = "192.168.233.2"
# HOST = "192.168.210.52"
# HOST = "192.168.233.83"
PORT = 5100


def get_req():
    global req
    # filePath = "/Users/user/Documents/project/PycharmProjects/call_ds/utils/tt"
    # readLogFile(filePath)
    path2 = "/Users/user/Documents/project/PycharmProjects/workAbout/call_ds/data/logs_beijing"
    f = open(path2)
    line = f.read()
    source = json.loads(line)
    dict1 = DictToClass()
    req = dict1.dict_to_object2(source)
    print type(req)
    # print json.dumps(req,default=lambda o:o.__dict__)
    # ft = FormatTime()
    # req.inner_search_type = 4
    # req.page_rank_attr = PageRankAttribute()
    # req.page_rank_attr.page_size = 100
    # req.product_attr.stay_date.check_in = ft.deltaDate(0)
    # req.product_attr.stay_date.check_out = ft.deltaDate(1)
    # regions = [101]
    # for region in regions:
    #     req.geo_attr.region_id = region
    #     # 获取列表页酒店id
    #     for i in xrange(0, 20):
    #         req.page_rank_attr.page_index = i
    #         req.inner_search_type = 1
            # res = process(req)
    return req

def process():
    req = get_req()
    send = Send.SendMessage(HOST,PORT)
    res = send.process(req)
    # print res.status.msg
    return res


if __name__ == '__main__':
    res = process()
    print res
    # print res.status.msg
    print json.dumps(res,default=lambda o:o.__dict__)
    result = ShowResult(req,res)
    # result.Product()
    result.statics()
    # print res