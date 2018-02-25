#!/usr/bin/env python
#coding:utf-8

def is_prime(num):
    if 2>=num>1:
        return True
    elif num>2:
        for i in range(2,num+1):
            if num%i==0 and i<num:
                return False
            elif num%i==0 and i==num:
                return True
    else:
        return False
#lambda version
f=lambda x:x>1 and not any (x%n==0 for n in range(2,x)) or x==1
