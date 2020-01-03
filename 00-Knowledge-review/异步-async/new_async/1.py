# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang
'''
# 老方法
import asyncio


@asyncio.coroutine
def hello():
    print("hello world")
    r = yield from asyncio.sleep(1)
    print("hello again!")


loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
'''
# 新方法
import asyncio


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")


loop = asyncio.get_event_loop()
tasks = [hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
