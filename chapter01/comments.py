# coding=utf-8
"""
研究Python程序注释问题
Version: 0.1
Author: huijz
Date: 2020-08-04

单行注释1： # -*- coding:UTF-8 -*-
多行注释2：''' 这是多行注释，使用单引号 '''
"""
print ("Hello, Python!")
# 第一个注释
print ("Hello, Word!")  # 第二个注释
'''
这是多行注释，使用单引号。
这是多行注释，使用单引号。
'''
"""
这是多行注释，使用双引号。
这是多行注释，使用双引号。
这是多行注释，使用双引号。
"""
# 行和缩进
if True:
    print ("True")
else:
    print ("False")

if True:
    print ("Answer")
    print ("True")
else:
    print ("Answer")
    # 没有严格缩进，在执行时会报错
# print ("False")

'''
多行语句

'''
total = item_one + \
        item_two + \
        item_three

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

'''
Python 引号

'''
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""
