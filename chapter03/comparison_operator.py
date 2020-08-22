# coding=utf-8
"""
Python所有比较运算符的操作
Version: 0.1
Author: huijz
Date: 2020-08-22
"""
a, b, c = 21, 10, 0
if a == b:
    print "1 a等于b"
else:
    print "1 a不等于b"
if a != b:
    print "2 a不等于b"
else:
    print "2 a 等于b"
if a <> b:
    print "3 a 不等于b"
else:
    print "3 a等于b"

if a < b:
    print "4 a小于b"
else:
    print "4 a大于等于b"
if a > b:
    print "5 a大于b"
else:
    print "5 a小于等于b"

# 修改a和b的值
a = 5
b = 20
if a <= b:
    print "a 小于等于b"
else:
    print "a 大于b"
if b >= a:
    print "b 大于等于a"
else:
    print "b 小于a"
