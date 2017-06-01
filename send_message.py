#-*-coding:utf-8-*-
__author__='ting.yin'

import re,json,hashlib
import urllib,urllib2
import requests
from collections import namedtuple,defaultdict

class InterfaceTest():
    def __init__(self,name,url,header):
        self.url = url
        self.filename = name
        self.header = header

    def process_source_data(self):
        three_item = []
        DCPrice = namedtuple("DC",['shotel_id','sroom_id','rateplan_id','Details'],)
        priceDetail = namedtuple('detail',['currencyType','startDate','endDate','totalcost'])
        with open("./data/request") as f:
            detail = []
            request = []
            for line in f.readlines(1000):
                t1 = re.split(r'[\s|##]+',line)[:3]
                if t1 == three_item:
                    pd = priceDetail._make(re.split(r'[\s|##]+',line)[3:7])
                    detail.append(pd)
                    print 'equal_detail: ',detail
                else:
                    print 'detail: ',re.split(r'[\s|##]+', line)[3:7]
                    three_item = t1
                    print 'three-item: ',three_item
                    pd = priceDetail._make(re.split(r'[\s|##]+',line)[3:7])
                    detail.append(pd)
                    request.append(three_item[0])
                    request.append(three_item[1])
                    request.append(three_item[2])
                    request.extend(detail)
                    dc = DCPrice._make(request)
                    print 'dc: ',dc
                    print '_dict_: ',type(dc._asdict()),dc._asdict()

    def get_detail(self,line):
        detail = defaultdict()
        detail['priceMode'] = re.split(r'[\s|##]+', line)[5]
        detail['currencyType'] = re.split(r'[\s|##]+', line)[6]
        detail['startDate'] = re.split(r'[\s|##]+', line)[7]
        detail['endDate'] = re.split(r'[\s|##]+', line)[8]
        detail['totalCost'] = re.split(r'[\s|##]+', line)[9]
        detail['totalCostOrigin'] = re.split(r'[\s|##]+', line)[10]
        detail['totalPrice'] = re.split(r'[\s|##]+', line)[11]
        detail['totalPriceOrigin'] = re.split(r'[\s|##]+', line)[12]
        detail['version'] = re.split(r'[\s|##]+', line)[13]
        return detail

    def source_data(self,filename):
        request = defaultdict(lambda :'N/a')
        reqs = []
        i = 0
        dt = []
        with open(filename) as f:
            for line in f.readlines(100):
                if cmp(re.split(r'[\s|##]+',line)[0],request['hotelId']) == 0 and \
                        cmp(re.split(r'[\s|##]+', line)[1],request['sroomId']) == 0 and \
                        cmp(re.split(r'[\s|##]+', line)[2],request['rateplanId']) == 0:
                    i += 1
                    dt.append(self.get_detail(line))
                else:
                    if i != 0:
                        # 中途遇到新的一条
                        request['priceDetails'] = dt
                        reqs.append(request)
                        dt = []
                        print 'internal:',json.dumps(request,ensure_ascii=True)
                        i = 0
                    request = defaultdict(lambda: 'N/a')
                    request['hotelId'] = re.split(r'[\s|##]+',line)[0]
                    request['sroomId'] = re.split(r'[\s|##]+',line)[1]
                    request['rateplanId'] = re.split(r'[\s|##]+',line)[2]
                    request['onLineSearchType'] = re.split(r'[\s|##]+',line)[3]
                    request['createOrderTime'] = re.split(r'[\s|##]+',line)[4]
                    request['traceId'] = hashlib.md5('hello').hexdigest()
                    dt.append(self.get_detail(line))
                    i += 1
            # 最后一条
            if i != 0:
                request['priceDetails'] = dt
                reqs.append(request)
                return reqs
                print 'end:',request
            print '',json.dumps(request,ensure_ascii=True)

    def build_message(self):
        request = defaultdict(lambda :'n/a')
        request['from'] = 'ting.yin'
        request['logId'] = hashlib.md5('yes').hexdigest()
        request['traceId'] = hashlib.md5('no').hexdigest()
        request['realRequest'] = self.source_data(self.filename)
        # print '',json.dumps(request,ensure_ascii=True)
        print 'requestJson:'+str(request)
        return 'requestJson:'+str(request)
        # return request
        data = open(self.filename).read()
        return json.loads(data)

    def send_message(self):
        data = self.build_message()
        print type(data),data
        return
        # 方法一
        r = requests.post(self.url,data=data,headers=self.header)
        print r
        # req_data = urllib.urlencode(data)
        # # req = urllib2.Request(url=self.url,data=req_data)
        # res = urllib.urlopen(self.url,data=req_data)
        # print res.read()

if __name__ == "__main__":
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    url = "http://192.168.233.113:9037/rest/com/elong/hotel/goods/message/common/entity/DCPriceInBatchReq"
    it = InterfaceTest('./data/request',url,header)
    # it.build_message()
    it.send_message()
