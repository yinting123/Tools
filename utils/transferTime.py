#-*-coding:utf-*-
__author__='ting.yin'

def transfer(time):
    hour = time / 3600
    min = (time % 3600) / 60
    sec = (time % 3600) % 60
    print "time : %s ,transferd: %d:%d:%d" %(time,hour,min,sec)

if __name__=="__main__":
    transfer(17265)
    transfer(17279)
    # transfer(17265)
