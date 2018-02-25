#!/usr/bin/env python
#coding:utf-8

def chained(functions):
    """
     chained([a,b,c,d])(input)
     and yield as below:
     d(c(b(a(input))))
    """
    def f(inputv):
        for func in functions:
            inputv = func(inputv)
        return inputv
    return f
#reversed and get string title 
[x[::-1].title() for x in ["lorem","ipsum","dolor"]]

