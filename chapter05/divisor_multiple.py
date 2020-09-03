# coding=utf-8
"""
@desc：求最大公约数，和最小公倍数
@auth： huijz
@date: 2020-09-02
@mail: huijz81117@gmail.com
"""
x = int(input("x="))
y = int(input("y="))
if x > y:
    x, y = y, x
print range(x, 0, -1)
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
