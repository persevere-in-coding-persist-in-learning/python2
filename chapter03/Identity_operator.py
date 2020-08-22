# coding=utf-8
"""
Python所有身份运算符的操作
Version: 0.1
Author: huijz
Date: 2020-08-22
"""
a, b = 20, 20

c, d = "张三", "张三"

if a is b:
    print "1 a和b有相同的标志", id(a), id(b)
else:
    print "1 a和b没有相同的标志", id(a), id(b)

if c is d:
    print "2 c和d有相同的标志", id(c), id(d)
else:
    print "2 c和d没有相同的标志", id(c), id(d)

if a is not b:
    print "3 a和b没有相同的标志", id(a), id(b)
else:
    print "3 a和b有相同的标志", id(a), id(b)

if c is not b:
    print "4 c和b没有相同的标志", id(c), id(b)
else:
    print "4 c和b有相同的标志", id(c), id(b)
