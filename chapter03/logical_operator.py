# coding=utf-8
"""
Python所有逻辑运算符的操作
Version: 0.1
Author: huijz
Date: 2020-08-22
"""
a, b, c = 10, 20, 0
if a and b:
    print "1 变量a 和变量 b 都为true"
else:
    print "1 变量a 和变量 b 至少有一个不为true"
if a or b:
    print "2 变量a 和变量 b 至少有一个为true"
else:
    print "2 变量a 和变量b 都不为true"
if a and c:
    print "3 变量a 和 c 都为true"
else:
    print "3 变量a 和 c 至少有一个不为true"
if a or c:
    print "4 变量 a 和 c 至少有一个为true"
else:
    print "4 变量 a 和 c 都不为true"
if not (a and c):
    print "5 变量a 和 c 至少有一个不为true"
else:
    print "5 变量a 和 c 都为true"
