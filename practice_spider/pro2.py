import math

km = math.ceil(float(input('请输入坐车的公里数:可以输入小数')))


def calculate(km):
    if km <= 3:
        money = 15
    elif 3 < km <= 15:
        money = 15 + (km - 3) * 3
    elif km > 15:
        money = 15 + 12 * 3 + (km - 15) * 5
    print('本次打车费用为:%d元' % money)


calculate(km)
