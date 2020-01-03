# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import asyncio
import time


def count_time(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        return end_time - start_time

    return inner


# @count_time
@asyncio.coroutine
def hello():
    print("Hello wprld!")
    # 异步调用asyncio.sleep(1)
    step = yield from asyncio.sleep(1)
    print("Hello adain!")


# 获取Evenloop
loop = asyncio.get_event_loop()
# 执行Evenloop
loop.run_until_complete(hello())
loop.close()
