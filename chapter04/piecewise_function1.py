# coding=utf-8
"""
@Desc:分段函数求值
        3x - 5  (x > 1)
f(x) =  x + 2   (-1 <= x <= 1)
        5x + 3  (x < -1)
@Version: 0.1
@Author: huijz
@Mail: huijz8117@gmail.com
@Date: 2020-08-24
"""
x = float(input('x='))
if x > 1:
    print "f(" + str(x) + ")=%.f" % (3 * x - 5)
elif -1 <= x <= 1:
    print "f(" + str(x) + ")=%.f" % (x + 2)
elif x < -1:
    print "f(" + str(x) + ")=%.f" % (5 * x + 3)






