#!/usr/bin/env python
#coding:utf-8

"""
__def__(self):
析构器，不实现语句:def x,定义当一个对象进行垃圾回收时候的行为，当一个对象删除的时候需要更多清洁工作此方法会很有用。比如套接字或者文件对象，
如下，打开一个文件并当退出时__del__操作关闭文本流
"""

class FileObject:
    """给文件对象进行包装从而确认在删除时文件流关闭"""
    def __init__(self,filepath="~",filename="sample.txt"):
        self.file=open(filepath.join(filename),"r+")#读写模式打开一个文件
    def __del__(self):
        self.file.close()
        del self.file
#multiplication based on class

def Foo(object):
    def __init__(self):
        self.value=2.523523
    def __mul__(self,other):#multiplication
        return self.value*other
    def __rmul__(self,other):#be multipled
        return other*self.value
    def __add__(self,other):#plus
        return self.value+other
    def __radd__(self,other):#be added
        return other+self.value
    def __div__(self,other):#divide
        return self.value/other
    def __rdiv__(self,other):#be divided
        return other/self.value
    def __sub__(self,other):#substract
        return self.value-other
    def __rsub__(self,other):#be substracted
        return other-self.value
    def __floordiv__(self,other):#floor divide
        return self.value//other
    def __rfoordiv__(self,other):#be floordivided
        return other//self.value
    def __mod__(self,other):#mod
        return self.value%other
    def __rmod__(self,other):#be moded
        return other%self.value
    def __truediv__(self,other):#need import division from __future__
        return self.value/other
    def __rtruediv__(self,other):#same as above
        return other/self.value
    def __gt__(self,other):
        return len(self.value)
    def __len__(self):#len(instance)
        return self.value
    def __abs__(self):#absolute value
        return abs(self.value)
    def __neg__(self):
        return -self.value
    def __pos__(self):
        return +self.value
    def __round__(self,n=2):
        return self.value
    def __float__(self):
        return self.value
    def __repr__(self):
        """If we did not implement  __repr__ , vector instances would be shown in the console like  <Vector object at 0x10e100070> """
        return "return value to interpreter,__str__ uses print ,when __str__ is not implemented ,interpreter will use __repr__ instead."

a=Foo()
a*7#14
8*a#16
"""
用于比较的魔法方法
__cmp__(self,other),__cmp__是最基本的用于比较的魔法方法，
"""
