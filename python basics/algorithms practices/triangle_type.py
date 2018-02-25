#!/usr/bin/env python
#coding:utf-8

def triangle_type(a, b, c):
    l=sorted([a,b,c])
    if a+b>c and a+c>b and b+c>a: 
        if l[0]**2+l[1]**2==l[2]**2:
            return 2#直角
        if l[0]**2+l[1]**2>l[2]**2:
            return 1#锐解
        if l[0]**2+l[1]**2<l[2]**2:
            return 3#钝角
    else:
        return 0#不勾成三角形
