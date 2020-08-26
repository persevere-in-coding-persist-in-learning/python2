# coding=utf-8
"""
@desc: 判断输入的边长能否构成三角形如果能则计算出三角形的周长和面积
@version: 1.0
@author: huijz
@mail: huijz8117@gmail.com
@date: 2020-08-26
"""
import math

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and a + c > b and b + c > a:
    print "周长:%f" % (a + b + c)
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print "面积:%f" % area
else:
    print "不能构成三角形"
