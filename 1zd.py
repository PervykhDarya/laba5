#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input())
b = int(input())
c = int(input())

m = a
if m < b:
    m = b
if m < c:
    m = c

print(m)