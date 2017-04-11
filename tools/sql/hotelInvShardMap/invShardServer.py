#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys, glob
cur_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(cur_path + "/gen-py")

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.protocol import TCompactProtocol

from ResultQuery import MySqlQueryService
from ResultQuery.ttypes import *
from ResultQuery.constants import *


class SHotelInventoryShard:
    __host = '192.168.67.34'
    __port = 9092
    __dbname = 'inventory'
    __keyname = '@hotel_id'

    @classmethod
    def SetHost(cls, host, port):
        cls.__host = host
        cls.__port = port

    @classmethod
    def GetShardId(cls, shotel_id):
        try:
            socket = TSocket.TSocket(cls.__host, cls.__port)
            transport = TTransport.TFramedTransport(socket)
            protocol = TCompactProtocol.TCompactProtocol(transport)
            client = MySqlQueryService.Client(protocol)
            transport.open()
            dValue = DataValue()
            dValue.data_type = 8
            dValue.data_value = shotel_id
            shard_id = client.GetPartitionID(cls.__dbname, cls.__keyname, dValue)
        except Exception,ex:
            print Exception,':',ex
        else:
            return shard_id

    @classmethod
    def GetShardIds(cls, shotel_ids):
        try:
            socket = TSocket.TSocket(cls.__host, cls.__port)
            transport = TTransport.TFramedTransport(socket)
            protocol = TCompactProtocol.TCompactProtocol(transport)
            client = MySqlQueryService.Client(protocol)
            transport.open()
            dValue_list = []
            for id in shotel_ids:
                dValue = DataValue()
                dValue.data_type = 8
                dValue.data_value = id
                dValue_list.append(dValue)
            shard_id_set = client.GetPartitionIDSet(cls.__dbname, cls.__keyname, dValue_list)
        except Exception,ex:
            print Exception,':',ex
            return
        else:
            return cls.PartitionIDSets2Dict(shard_id_set)

    @classmethod
    def PartitionIDSets2Dict(cls, pIDSets):
        d = dict()
        for pIDSet in pIDSets.sets:
            id_list = []
            for dataValue in pIDSet.value_list:
                id_list.append(dataValue.data_value)
            d_tmp = {pIDSet.shard_id : id_list}
            d.update(d_tmp)
        return d
