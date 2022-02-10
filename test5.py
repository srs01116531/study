#!/usr/bin/python
# -*- coding: UTF-8 -*-


def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print str
   return

# 调用函数
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")

def print_func( par ):
   print "Hello : ", par
   return
print_func( "saf")



# 现在可以调用模块里包含的函数了
support.print_func("Runoob")