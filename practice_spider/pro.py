menu_list = [{"id": 1, "name": "1.蛋炒面", "price": "12", "¥": "元"},
             {"id": 2, "name": "2.回勺面", "price": "15", "¥": "元"},
             {"id": 3, "name": "3.刀削面", "price": "8", "¥": "元"},
             {"id": 4, "name": "4.饸饹面", "price": "9", "¥": "元"}]
order_list = []
print('===========公司食堂开业啦，欢迎大家============')
print('今日菜单')
for menu in menu_list:
    print(menu.get("name"), menu.get("price"), menu.get("¥"))
while True:
    print('=' * 50)
    print('1.点餐\n2.取消点菜\n3.确认菜单\n4.结账')
    choose = int(input('1请选择服务：'))
    if choose == 1:
        while True:
            menu_add = input('请输入菜名编号或输入n结束：')
            if menu_add is not str:
                # if menu_add != 'n':
                for m in menu_list:
                    if m.get('id') == int(menu_add):
                        print(m)
                        order_list.append(m)
                        print("order_list:{}".format(order_list))
                        break
                    else:
                        print('输入错误1')
            else:
                print('点餐完毕')
                total_price = 0
                for order in order_list:
                    print(order.get("name"), order.get("price"), order.get("¥"))
                    total_price += int(order.get("price"))
                    print('本次用餐价格为：{}元'.format(total_price))
                break
    elif choose == 2:
        while True:
            menu_del = input('请输入要取消的菜名编号或输入o结束：')
            if menu_del != 'o':
                for n in order_list:
                    if n.get("id") == int(menu_del):
                        order_list.remove(n)
                        print('已取消')
                    else:
                        print('输入错误2')
                total_price = 0
                for order in order_list:
                    print(order.get("name"), order.get("price"), order.get("¥"))
                    total_price += int(order.get("price"))
                    print('本次用餐价格为：{}元'.format(total_price))
                break
    elif choose == 3:
        print('您点的菜为：')
        total_price = 0
        for order in order_list:
            print(order.get("name"), order.get("price"), order.get("¥"))
            total_price += int(order.get("price"))
            # print('
            print('本次用餐价格为：{}元'.format(total_price))
    elif choose == 4:
        print('您的消费菜单为：')
        total_price = 0
        for order in order_list:
            print(order.get("name"), order.get("price"), order.get("¥"))
            total_price += int(order.get("price"))
        print('本次用餐共计：{}元'.format(total_price))
        print('感谢您光临本店')
        break
