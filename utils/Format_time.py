__author__ = 'ting.yin'
#-*-coding:utf-8-*-

import time
from datetime import date as d1
from datetime import time as t1
from datetime import datetime as dt
from datetime import timedelta
import datetime
import re

class FormatTime:

    """
        1.设置特定日期
        2.指定日期，时间
        3.指定周有效
    """

    def __init__(self):
        self.today = dt.today()

    def timeTest(self):
        print time.time()
        """
        将时间戳改为tuple格式       时间戳 <————> tuple
        """
        print "-"*5,"tuple —— 时间戳","-"*5
        print time.gmtime(time.time())                                          #时间戳转tuple 差8小时
        print time.localtime(time.time())                                       #时间戳转tuple
        print time.mktime(time.localtime(time.time()))                          #tuple转换为时间戳

        """
        格式转换                  tuple < ———— > 指定格式
        """
        print "-"*5,"tuple —— 指定格式","-"*5
        print time.strftime('%Y%m%d%H%M%S',time.gmtime(time.time()))            #tuple转为指定格式
        print time.strptime('2016-11-26 10:00:00','%Y-%m-%d %H:%M:%S')          #将指定时间转换为tuple


        """
        入参为tuple
        """

        """
        入参为时间戳
        """

        print time.ctime(time.time())                                           #时间戳转换为固定格式
        print time.asctime(time.localtime(time.time()))                         #将tuple转换为固定格式的日期

    def specialDate(self):
        print '-'*5,'date操作','-'*5
        """
        生成对象
         更新对象，但不改变元对象属性
        """
        d = d1.today()
        print 'today: ',d

        dd = d.replace(2016,01,01)
        print d,dd
        print 'd.month',d.month
        """
        获取周
        格式化输出
        返回tuple
        """
        w = d.isoweekday()
        print 'weekday:',w
        print 'format: ',d.strftime('%Y:%m-%d')
        print 'iosformat: ',d.isoformat()

        print 'tuple : ',d.timetuple()



        """
        datetime
            创建对象，获取对象
            修改对象,组合对象
            转换为时间戳
        """
        print '-'*5,'datetime操作','-'*5
        print '对象1：', dt.today()
        print '对象2：', dt.now()
        print '对象3：',dt.utcnow()
        print '对象4：',dt.fromtimestamp(time.time())
        print '对象5：',dt.utcfromtimestamp(time.time())

        today = dt.today()

        print "tomorrow1 :", today.replace(today.year,today.month,today.day+1)
        print "tomorrow2 :",today + timedelta(days=30)

        print 'next hour:',today+ timedelta(hours=1.5)

        """
        time
            通过datetime获取对象
        """
        print '-'*5,'time操作','-'*5
        print 'time: ',today.time()

        print 'datetime转时间戳:',time.mktime(today.timetuple())

        """
        timedelta

        """
        print '-'*5,'timedelta操作','-'*5




    def change(self):
        t = time.time()
        print '当前时间: ',time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t))
        print '当前时间2: ',dt.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
        print '当前时间3: ',dt.utcfromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

    def Split_Date(self,str):
        """

        :param str:
        :return:
        """
        str1 = str.split('-')
        return int(str1[0]),int(str1[1]),int(str1[2])
        # print  re.split(str,'-')[0],re.split(str,'-')[1],re.split(str,'-')[2]

    def Split_Time(self,str):
        str1 = str.split(':')
        return int(str1[0]),int(str1[1]),int(str1[2])

    def Special_Day(self,str):
        """
            @desc: 生成指定日期，年、月、日
            @:param     年、月、日
            @:return    date
        """
        year,month,day = self.Split_Date(str)

        date = self.today.date()
        print date.replace(year,month,day)
        return date.replace(year,month,day)


    def Special_Time(self,str,str2):
        """
        @desc: 生成指定时间的datetime对象
        @param： y 、m、d、hour、min、sec
        @return:  datetime

        """
        hour,min,sec = self.Split_Time(str2)
        tt= self.today.time().replace(hour,min,sec)
        dd = self.Special_Day(str)
        print  dt.combine(dd,tt)
        return dt.combine(dd,tt)

    def SetDate(self,str):
        print time.mktime(self.Special_Day(str).timetuple())
        return  time.mktime(self.Special_Day(str).timetuple())

    def SetTime(self,str1,str2):
        res = self.Special_Time(str1,str2)
        print time.mktime(res.timetuple())
        return time.mktime(res.timetuple())

    def SetTimeToday(self,str1):
        tt = self.today.time()
        dd = self.today.date()
        hour,min,sec= self.Split_Time(str1)
        tt = tt.replace(hour,min,int(sec))
        # print dt.fromtimestamp(int(time.mktime(dt.combine(dd,tt).timetuple())))
        # print dt.combine(dd,tt)
        return int(time.mktime(dt.combine(dd,tt).timetuple()))

    def yesterday(self):
        dd = self.today.date() + timedelta(days= -1)
        return int(time.mktime(dd.timetuple()))

    def Today(self):
        return int(time.mktime(self.today.timetuple()))

    def tommorrow(self):
        dd = self.today.date() + timedelta(days= 1)
        return int(time.mktime(dd.timetuple()))

    def deltaDate(self,delta):
        dd = self.today + timedelta(days=delta)
        return int(time.mktime(dd.timetuple()))



if __name__ == "__main__":
    mat = FormatTime()
    # mat.timeTest()
    # mat.specialDate()
    # mat.change()

    # mat.Split_Date('2016-10-29')
    # mat.Special_Day('2016-10-29')
    mat.SetDate('2016-10-29')
    mat.SetTime('2016-10-29','10:59:59')
    mat.SetTimeToday('10:59:59')