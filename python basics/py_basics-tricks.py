#!/usr/bin/env python
#coding:utf-8

#pack and uppack list in python

a,b=[1,2,3],[4,5,6]
#pack
c=zip(a,b)#[(1, 4), (2, 5), (3, 6)]
#unpack
d=zip(*c)#[(1,2,3),(4,5,6)]
#create iterator

#create the iterator with max value no more than 1000
class x(object):
	def __init__(self):
	    self.a=0
	    self.b=3
	def next(self):
	    self.a,self.b=self.b,self.a+self.b
	    if (self.b)>1000:raise StopIteration
	    return self.b
	def __iter__(self):
	    return self
#recursive
f=lambda x:x and f(x-1)*x or 1
print f(9)



#use magic method:
f = lambda x: reduce(int.__mul__, xrange(1, x + 1)) #int.__mul__=>x*y

#private attribute and access
class Secretive(object):
    def __inaccessible(self):
        print "Bet you can't see me.."
    def accessible(self):
        print "get secrect message is:"
        self.__inaccessible()

s=Secretive()
#can't access attribute directly
s.__inaccessible()#got exception AttributeError
#via bound method
s.accessible()
#另外一种访问私有变量的方式:
s._Secretive__inaccessible()

#fibonnacci
f=lambda x:x>=2 and f(x-2)+f(x-1) or x

#char and ascii 
number=ord("a")
char = chr(65)

#closure
def foo(x):
    def bar(y):
        return x+y
    return bar

#decorator based on closure
def func(fn):
    def wrapped(x):
        return fn(x)+2
    return wrapped#return closure func

@func
def funcwrap(x):
    return x*3

if __name__=="__main__":
    funcwrap(9)
