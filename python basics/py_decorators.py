#!/usr/bin python
#coding:utf-8

import time

#simple closurer
def outer_function(*args,**kwardgs):
    def get_parameters():
        def processpara():
            return sum(list(args)+kwardgs.values())
        return processpara
    return get_parameters()

#simple decorator
def every_10_seconds(func):
    def f():
        while True:
            time.sleep(10)
            func()
    return f

#decorator without arguments:when the decorated function is passed to the constructor ,the __call__()
#method is called whenever the decorated function is invoked.

class decoratorClass(object):
    def __init__(self,f):
        """no decorator arguments,"""
        self.f = f

    def __call__(self,*args):
        """when decorated function is called the __call__method is invoked."""
        self.f(*args)

#decorator with arguments

class decoratorWithArguments(object):
    def __init__(self,arg1,arg2,arg3):#here we get arguments from decorator
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        
    def __call__(self,f):
        def wrapped_f(*args):#get arguments from the function decorated
            f(*args)
        return wrapped_f

@decoratorWithArguments("hello","word","simon")  #just like we set default arguments value
def sayHello(a1,a2,a3,a4):
    print "sayhello arguments:",a1,a2,a3,a4

#funtion version:decorator with arguments

def decoratorWithArguments(arg1,arg2,arg3):#here we get arguments from decorator
    def wrap(f):
        def wrapped(*args):#get arguments from the function decorated
            f(*args)
        return wrapped
    return wrap

@decoratorWithArguments("hello","world","simon")
def sayHello(a1,a2,a3,a4):
    print "say hellow arguments:",a1,a2,a3,a4

def argumentize(n):
        def wrap(f):
            def wrapped(*args,**kws):
                return n*f(*args,**kws)
            return wrapped
        return wrap

@argumentize(2)
def function(a):
        return 10 + a

class doubleResult(object):
    def __init__(self,n):
        self.n = n

    def __call__(self,f):
        print self.n
        def wrap(*args,**kwds):
            return self.n*f(*args,**kwds)
        return wrap


@doubleResult(2)
def function(a):
    print 10 + a
    return 10 + a
    
if __name__ == "__main__":
    """
    @every_10_seconds
    def count():
        print "run at every 10 seconds."       
    count()
    """
    """def multiply(f, n):
        def aux(*xs, **kws):
            return n * f(*xs, **kws)
        return aux"""

    #print outer_function(1,2,3,a=2,b=6)()
    print function(4)
    
