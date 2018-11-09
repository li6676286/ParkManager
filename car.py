import time
from manager import ParkManage

class Car(ParkManage):
    """一个关于车的类"""
    def __init__(self,car_number,car_owner,contact_way,car_port):
        super(Car, self).__init__()
        self.car_number=car_number
        self.car_owner=car_owner
        self.contact_way=contact_way
        self.car_port =car_port
        self.entrance_time = 0
        self.exit_time = 0

    def __setitem__(self, key, value):
        self.__dict__[key]=value

    def slot_card(self):
        """根据时间计费"""
        park_time=time.mktime(time.strptime(self.exit_time)) - time.mktime(
            time.strptime(self.entrance_time))
        h=park_time//3600
        m=(park_time-h*3600)//60
        s=park_time-h*3600-m*60
        P_time="%.0f时%.0f分%.0f秒"%(h,m,s)
        consumption = ((park_time) / 3600) * 5
        print("车牌号为:%s\n停车时长:%s\n本次消费:%.2f元\n" % (self.car_number,P_time, consumption))

    def __str__(self):
        """返回字符串信息"""
        return "%s %s %s %s %s" %(self.car_number,self.car_owner,self.contact_way,self.car_port,self.entrance_time)