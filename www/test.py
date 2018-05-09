#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'PayneV'
'testing code'

import orm
from models import User,Blog,Comment
import asyncio


async def test():

    #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
    await orm.create_pool(loop=loop, host='192.168.0.24', port=3306, user='root', password='eland',db='awesome')

    #没有设置默认值的一个都不能少
    u = User(name='paynev', email='nxwzj0@126.com', passwd='728160', image='about:blank',id='1')

    await u.save()

# 获取EventLoop:
loop = asyncio.get_event_loop()

#把协程丢到EventLoop中执行
loop.run_until_complete(test())

#关闭EventLoop
loop.close()

'sql check code'
import mysql.connector 

conn=mysql.connector.connect(user='root', password='eland', database='awesome')
cursor=conn.cursor()
cursor.execute('select * from users')
data=cursor.fetchall()
print(data)