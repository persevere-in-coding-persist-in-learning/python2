# coding=utf-8
"""
@Desc: if else 练习 权限验证
@Version: 0.1
@Author: huijz
@Date: 2020-08-24
@Email: huijz@gmail.com
"""
import getpass

user_name = input('请输入用户名:')
user_pwd = input('请输入密码:')
# 如果希望输入口令时 终端中没有回显 可以使用getpass模块的getpass函数
# import getpass
# password = getpass.getpass('请输入口令: ')
if user_name == 'admin' and user_pwd == 123456:
    print "身份验证成功！"
else:
    print "身份验证失败！"
password = getpass.getpass('请输入口令: ')
if password != 123456:
    print "非法入侵!"
else:
    print "恭喜你成功登录!"
