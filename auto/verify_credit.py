__author__ = 'user'

import sys
sys.path.append("../")
sys.path.append("/Users/user/Documents/project/PycharmProjects/call_ds")

from cm.ttypes import *


def verify_credit(res):
    shotels = ["90000809","90000801","90176218"]
    rps = ["480901","480902","400927"]
    rooms = ["1","1","1"]
    product = ["90000809,1,480901","90000801,1,480902","90176218,1,400927"]
    for detail in res.hotels_details:
        for room in detail.room_types:
            for product in detail.room_types:

