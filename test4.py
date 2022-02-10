#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time  # 引入time模块

import time

localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为 :", localtime

# !/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar

cal = calendar.month(2022, 1)
print "以下输出2022年1月份的日历:"
print cal

def ChangeInt(a):
    a = 10
    print(a)

b = 2
ChangeInt(b)
print b


def printme(str):
    "打印任何传入的字符串"
    print str
    return


# 调用printme函数
printme('adas')