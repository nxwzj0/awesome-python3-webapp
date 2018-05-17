#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
# print('this','is','python!')
'''
input
'''
# name = input('please input your name:')
# print('Hello,',name)
'''
if
'''
# num = int(input('enter a number:'))
# if num >= 0:
#     print(num)
# elif num >= 60:
#     print('及格:',num)
# else:
#     print(-num)
'''
多行输出
'''
# print('''1
# 2
# 3''')
'''
格式化输出
占位符  替换内容
 %d	    整数
 %f	    浮点数
 %s	    字符串
 %x	    十六进制整数
'''
str = 'payne'
print('hello,%s,you have $%d' % (str,99999))
'''
list
'''
array = ['michael','jamie','thaons']
# 用len()函数可以获得list元素的个数
print("array's length:",len(array))
# 通过下标访问元素
array[0]# 'michael'
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
array[-1]# 'thaons'
# 加入
array.append('Adam')
# 插入
array.insert(1,'Jack')
# 删除
array.pop()# 最后一个元素出栈
array.pop(1)# 制定元素出栈
'''
tuple
'''
# 另一种有序列表叫元组：tuple。
array = ('Michael', 'Bob', 'Tracy')
# 现在，这个tuple不能变了，它也没有append()，insert()这样的方法。
# 其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，
# 但不能赋值成另外的元素。
# 定义一个只有一个元素的tuple
arr = (1,)
'''
for...in
'''
names = ['michael','jamie','thaons']
for name in names:
    print(name)
# 这段代码，会依次打印names的每一个元素
# 如果要计算1-100的整数之和，
#从1写到100有点困难，
#幸好Python提供一个range()函数，可以生成一个整数序列，
#再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
list(range(5))# [0, 1, 2, 3, 4]
# 0-100 sum
sum = 0
for i in range(101):
    sum = sum + i
print('0-100 sum:',sum)
'''
while
'''
i = 100
sum = 0
while i > 0:
    sum += i
    i = i - 1
print('0-100 sum:',sum)
'''
dict
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，
使用键-值（key-value）存储，具有极快的查找速度。
'''
map = {'a':1,'b':2}
map['a']# 1
# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
# >>> 'c' in map
# False
# 二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
# map.get('c') # None
# map.get('c',-1) # -1
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除
'''
function
'''
def my_abs(num):
    if not isinstance(num,(int,float)):
        raise TypeError('bad input element!')
    if num >= 0:
        return num
    else:
        return -num
print(my_abs(9))
'''
do nothing function
'''
def nop():
    pass

def trim(s=''):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s

if trim('hello  ') != 'hello':
    print('测试失败!1')
elif trim('  hello') != 'hello':
    print('测试失败!2')
elif trim('  hello  ') != 'hello':
    print('测试失败!3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!4')
elif trim('') != '':
    print('测试失败!5')
elif trim('    ') != '':
    print('测试失败!6')
else:
    print('测试成功!')

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    leng = len(L)
    temp = -1
    if leng == 0:
        return (None,None)
    elif L[0] == L[-1]:
        return (L[0],L[-1])
    for i in list(range(leng-1)):
        for j in list(range(leng-1-i)):
            if L[j] > L[j+1]:
                temp =L[j+1] 
                L[j+1] = L[j]
                L[j] = temp
    return (L[0],L[-1])
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')

class Screen(object):
    def __init__(self):
        _width = 0
        _height = 0
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,val):
        self._width = val
    @property
    def height(self):
        return self._width
    @height.setter
    def height(self,val):
        self._height = val
    @property
    def resolution(self):
        return self._width * self._height            

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

def name_of_email(addr = 'zijian.wei@newtouch.cn'):
    test = r'^([0-9a-zA-z\.\_\s\<\>]+)(\@[0-9a-zA-z\.\_]+\.[0-9a-zA-z]+)$'
    name = re.match(test,addr).group(1)
    test = r'\<?([0-9a-zA-z\s\.\_]*)\>?([0-9a-zA-z\s\.\_])*'
    return re.match(test,name).group(1)
# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')