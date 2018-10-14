import time

class ParkManage(object):
    """创建一个关于停车的类"""
    def __init__(self,max_car=100,):  #定义最大停车辆数
        self.max_car=max_car
        self.car_list = []
        self.cur_car=len(self.car_list)


    def info(self):
        """ #显示系统功能信息"""
        print("""
        —————————————————————————
        |***欢迎进入车辆管理系统***|
        —————————————————————————    
{1}                                    
{2}           1)车辆入库登记{3}{2}
{0}                                  
{2}           2)查询车辆信息{3}{2}
{0}
{2}           3)车辆出库登记{3}{2}
{0}
{2}              4)退出系统{3}{2}
{1}
        """.format("-"*40,"="*40,"|"," "*16))

    def add_car(self,car):
        """#车辆入库登记"""
        entrance_time = time.ctime()
        car["entrance_time"]=entrance_time
        for Car in self.car_list:
            if Car.car_number == car.car_number:
                print("车牌号信息有误，重新输入")
                break
        else:
            self.car_list.append(car)
            print("车牌号为%s的车入库成功" %car.car_number)

    def search_By_Number(self):
        """#按车牌号查询"""
        car_number=input("请输入你您要查找的车牌号：")
        for car in self.car_list:
            if car.car_number==car_number:
                print(car)
                break
        else:
            print("未找到车牌号为%s的车辆" %car_number)

    def search_By_Port(self,car_port):
        """#按车位号查询"""
        for car in self.car_list:
            if car.car_port==car_port:
                return True
            else:
                return False    

    def searchCar(self):
        self.search_By_Number()

    def delete_car(self,car):
        """车辆出库登记"""
        exit_time=time.ctime()
        car["exit_time"]=exit_time
        car.slot_card()
        self.car_list.remove(car)
        print("车牌号为%s的车辆成功出库"%car.car_number)
