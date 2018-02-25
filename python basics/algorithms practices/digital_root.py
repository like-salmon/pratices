#!/usr/bin/env python
#coding:utf-8

def digital_root(n):
    return n%9 or n and 9

#or
def parseint(seq):
	l="+".join(list(str(seq)))
	r=eval(l)
	if len(str(r))==1:return r
	return parseint(r)#await result to be returned
