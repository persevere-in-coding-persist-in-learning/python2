# coding=utf-8
"""
Python所有赋值运算符的操作
Version: 0.1
Author: huijz
Date: 2020-08-22
"""
a, b, c = 10, 21, 0
c = a + b
print "1-c的值：", c
c += a
print "2-c的值：", c
c *= a
print "3-c的值：", c
c /= a
print "4-c的值：", c
c = 2
c %= a
print "5-c 的值：", c
c **= a
print "6-c的值:", c
c //= a
print "7-c的值:", c
