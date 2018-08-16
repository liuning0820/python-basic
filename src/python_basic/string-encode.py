#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ord? build in funciton. Return the Unicode code point for a one-character string.
print(ord('H'))


s = 'Python-中文'
print(s)
b = s.encode('utf-8')  # by default, encoding='utf-8'
print(b)
print(b.decode()) # by default, encoding='utf-8'
print(b.decode('utf-8'))