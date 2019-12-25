# !/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding:utf-8 -*-
# @Author : Jiazhixiang


import asyncio


async def main():
    print("hello ...")
    await asyncio.sleep(1)
    print("... world!")


asyncio.run(main())
