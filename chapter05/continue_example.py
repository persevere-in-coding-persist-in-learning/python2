# coding=utf-8
"""
@desc: continue语句练习
@auth：huijz
@date: 2020-09-03
@version: 0.1
@email: huijz8117@mail.com
"""
for letter in "i love Python":  # 第一个实例
    if letter == 'h':
        continue
    print '当前字母：', letter

count = 10
while count > 0:  # 第二个实例
    count = count - 1
    if count < 5:
        continue
    print "当前count:", count
print "GoodBye"
