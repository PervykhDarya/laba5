#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(10,99):
    a = i//10
    b = i % 10
    if i % (a + b) == 0:
      print(i)
