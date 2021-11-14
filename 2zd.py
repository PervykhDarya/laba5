#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = int(input("Enter c:"))

    if (a % 2 == 1) or (b % 2 == 1) or(c % 2 == 1):
        print("Есть нечётное число")
    else:
        print("Все числа чётные")