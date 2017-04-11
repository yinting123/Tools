#-*-coding:utf-8-*-
__author__ = 'ting.yin'

import sys
import init
from cm.ttypes import *
from thrift.protocol import TCompactProtocol,TBinaryProtocol
from thrift.transport import TSocket,TTransport
from thriftproxy.ThriftProxy import Client
from thrift import Thrift
import  multiprocessing

# HOST='192.168.233.17'
HOST = "10.39.18.58"
PORT= 5100

class SendMessage():
    def __init__(self,HOST,PORT):
        self.host = HOST
        self.port = PORT
    def process(self, req):
        try:
            socket = TSocket.TSocket(self.host, self.port)
            #socket = TSocket.TSocket('192.168.35.37', 5555)
            #socket = TSocket.TSocket('10.39.18.58', 5100)
            transport = TTransport.TFramedTransport(socket)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            # protocol = TCompactProtocol.TCompactProtocol(transport)
            client = Client(protocol)
            transport.open()

            res = client.SearchInner(req)
            transport.close()
            return res
        except Thrift.TException ,e:
            print e.message

    def process_service(self,req):
        return

    def multi_process(func, reqs, num):
        pools = multiprocessing.Pool(num)
        pools.map(func, reqs)
        pools.close()
        pools.join()
