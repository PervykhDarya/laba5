#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))

    if (a > b) and (a > c):
        print ("Наибольшее: ", a)
    elif (b > a) and (b > c):
        print("Наибольшее: ", b)
    else:
        print ("Наибольшее: ", c)