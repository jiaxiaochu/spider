class Bike:
    def __init__(self, ID, age, state=0):
        # 单车初始化
        self.ID = ID
        self.age = age
        self.state = state

    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '【自行车】车辆编号%s，已经运行%d年，车辆状态：%s' % (self.ID, self.age, status)


class Motorbike(Bike):
    # 增加参数
    def __init__(self, ID, age, petrol='92', state=0):
        Bike.__init__(self, ID, age, state=0)  # 继承父类Bike
        self.petrol = petrol  # 增加属性

    # 修订方法
    def __str__(self):
        if self.state == 0:
            status = '待租借'
        else:
            status = '租借中'
        return '【摩托车】车辆编号%s，已经运行%d年，使用%s号汽油，车辆状态：%s' % (self.ID, self.age, self.petrol, status)


Motorbike(1, 2)
