#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @FileName  :test1.py
# @Time      :2021/12/28 22:44
# @Author    :wangxinyu
# description：
import sys, keyboard
def func():
    str1 = sys.stdin.readline().lower()
    print(f"type(str1):{type(str1)}\nstr1:{str1}")



def unit_test():
    func()


if __name__ == "__main__":
    print('*' * 10 + 'start' + '*' * 10)
    unit_test()
    print('*' * 10 + 'end' + '*' * 10)
