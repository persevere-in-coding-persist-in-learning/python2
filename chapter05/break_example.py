# coding=utf-8
"""
@desc: break语句练习
@auth: huijz
@date: 2020-09-03
@version: 1.0
@email: huijz8117@mail.com
"""
for letter in "huijz excise Python":  # 第一个实例
    if letter == 'P':
        print "当前letter是：%s" % letter
        break
var = 10  # 第二个实例
while var > 1:
    print '当前的var是：%d' % var
    var = var - 1
    if var == 5:
        break
print "GoodBye!"
