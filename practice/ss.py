from pymysql import *


def main():
    # 创建Connection连接
    conn = connect(host='rm-2ze03u1v79619rwt5o.mysql.rds.aliyuncs.com', port=3306, user='wucongwen',
                   password='UyTflfZqoITBef6J3pVtrGsalUmznQr6', database='kkb-cloud-vipcourse', charset='utf8')
    # 获得Cursor对象
    cs1 = conn.cursor()
    # 执行select语句，并返回受影响的行数：查询一条数据
    count = cs1.execute('select passback_params from`kkb-cloud-vipcourse`.`vip_order` limit 178000, 1000')
    # 打印受影响的行数
    print("查询到%d条数据:" % count)

    result = cs1.fetchone()
    print(result)

    # for i in range(count):
    #     # 获取查询的结果
    #     result = cs1.fetchone()
    #     # 打印查询的结果
    #     print(result)
    #     # 获取查询的结果

    # 关闭Cursor对象
    cs1.close()
    conn.close()


if __name__ == '__main__':
    main()
