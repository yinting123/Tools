#-*-coding:utf-8-*-

import redis

class Redis():

    def __init__(self,host,port):
        self.client = redis.Redis(host=host,port=port)

    def get(self,key):
        print self.client.get(key)

    def delete(self,key):
        self.client.delete(key)


if __name__=="__main__":
    redis = Redis("192.168.233.17",6379)
    redis.get("shopper_50401025_50401140")
    redis.delete("shopper_50401025_50401140")
    redis.get("shopper_50401025_50401140")
