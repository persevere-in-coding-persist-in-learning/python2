# coding=utf-8
"""
Python变量
Version: 0.1
Author: huijz
Date: 2020-08-05
1.使用input函数输入
使用int()进行类型转换
用占位符格式化输出的字符串

2.使用type()检查变量的类型
"""
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name

a = 2
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d %% %d = %d' % (a, b, a % b))
print('%d ** %d = %d' % (a, b, a ** b))

a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。
a = b = c = 1
print a, b, c
# 也可以为多个对象指定多个变量
a, b, c = 1, 2, "john"
print a, b, c

a = 'Hello World!'

print a  # 输出完整字符串
print a[0]  # 输出字符串中的第一个字符
print a[2:5]  # 输出字符串中第三个至第六个之间的字符串
print a[2:]  # 输出从第三个字符开始的字符串
print a * 2  # 输出字符串两次
print a + "TEST"  # 输出连接的字符串
print a[0:9:2]  # 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 0 到索引 9 的位置并设置为步长为 2（间隔一个位置）来截取字符串：
