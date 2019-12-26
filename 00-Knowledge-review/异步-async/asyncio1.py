# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
import time
import asyncio

now = lambda: time.time()


# print(now())


async def do_some_work(x):
    print("waiting:", x)
start = now()
coroutine = do_some_work(2)
print(coroutine)
