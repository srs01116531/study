#!/usr/bin/python
# -*- coding: UTF-8 -*-

def function():
    print('This is a function')
    a = 1+2
    print(a)
function()

def func(a, b):
    c = a+b
    print('the c is', c)
func(2,3)

def sale_car(price, color='red', brand='carmy', is_second_hand=True):
    print('price', price,
          'color', color,
          'brand', brand,
          'is_second_hand', is_second_hand,)
sale_car(1000, 'red', 'carmy', True)