# coding=utf-8
"""
@desc: 判断一个数是不是素数
质数又称素数。一个大于1的自然数，除了1和它自身外，不能被其他自然数整除的数叫做质数；
否则称为合数（规定1既不是质数也不是合数）。


@auth: huijz
@date: 2020-09-02
@mail: huijz8117@gmail.com
"""
from math import sqrt

num = int(input("请输入一个正整数："))
end = int(sqrt(num))
is_prime = True
print end + 1
for x in range(2, end + 1):
    if num % 2 == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print "%d是素数" % num
else:
    print "%d不是素数" % num
