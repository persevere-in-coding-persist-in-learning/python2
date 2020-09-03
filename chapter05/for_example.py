# coding=utf-8
"""
@desc: for循环结构练习
@auth: huijz
@date:2020-09-02
@email: 670478647@qq.com
"""

for letter in "python":  # 第一个实例
    print "当前字母：", letter

fruits = ['香蕉', '橘子', '苹果', '桃子']
for fruit in fruits:  # 第二个实例
    print 'fruit:', fruit

# 通过序列索引迭代
fruits = ['peach', 'orange', 'apple', 'mongo']
for index in range(len(fruits)):
    print "当前水果：", fruits[index]
print range(10), range(2, 10), range(3, 1)

'''循环使用 else 语句在 python 中，for … else 表示这样的意思，for 中的语句和普通的没有区别，
else 中的语句会在循环正常执行完（即 for 不是通过 break 跳出而中断的）的情况下执行，while … else 也是一样。'''

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print '%d 等于 %d * %d' % (num, i, j)
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print num, '是一个质数'
