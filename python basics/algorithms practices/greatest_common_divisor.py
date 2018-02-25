#!/usr/bin/env python
#coding:utf-8

def nbr_of_laps(x, y):
    """两个数的乘积等于最大公因数与最小公倍数的乘积"""
    mn,man=min(x,y),max(x,y)
    n1=man
    n2=mn
    mul=mn*man
    while(n2!=0):
        gcd=n1%n2
        n1=n2#to get the greatest common divisor
        n2=gcd
    nmn=mul/n1#get the least common multiple
    return [nmn/x,nmn/y]

def nbr_of_laps_a(x, y):
    def gcd(a, b):
      if b == 0: return a
      return gcd(b, a % b)
    z = gcd(x, y)
    return [x * y / z / x, x * y / z / y]
