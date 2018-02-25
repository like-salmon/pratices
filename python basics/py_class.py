#!/usr/bin/env python
#coding:utf-8

#class's namespace


class Foo(object):
    bar = True
#以上相当于:
Foo = type('Foo',(),{"bar":True})

class FooChild(Foo):
    pass
def echo_bar(self):
    print (self.bar)#继承的属性不写也能访问到

"""
但是如果父类调用__init__方法，子类继承父类的构造函数，需要使用父类的构造函数，或者使用super(current_class,self)方法

class FooChild(Foo):
    def __init__(self):
        Foo.__init__(self)
        #或者:
        super(Foo,self).__init__()
        
        self.anotherbar=True
"""
#以上相当于
FooChild=type("FooChild",(Foo,),{"echo_bar":echo_bar})#type定义三个参数:新的对象名称，新的对象继承自某类名称，新的对象的属性
#python的动态类型:

a=FooChild()
#实例化后赋予属性给类，实例依然能访问到
def echo_more_bar(self):
    print "another method!"
a.echo_more=echo_more_bar
a.echo_more()#another method!
#每个类都有一个属性__class__，用于检测所属的类型
age=36
name="simon"
age.__class__#<type 'int'>
name.__class__#<type 'str'>
echo_more_bar.__class__#<type 'function'>
a.__class__#<type '__main__.FooChild'>

#任意对象的__class__
age.__class__.__class__#<type 'type'>
name.__class__.__class__#<type 'type'>
#由此可见__metaclass__ type主要是用于创建对象

"""
元类构建类的过程:
class Foo(Bar):
    pass
1.查找是否Foo里面定义了__metaclass__，如果有，在内存中创建类对象，使用__metaclass__里面定义的规则
2.如果没有，则在模块层级查找__metaclass__,如果有，则使用old-style的类对象元素去创建对象
3.如果模块层级也没有定义__metaclass__，则使用Bar(第一个父类)的元素，去创建类对象
4.Bar对象的__metaclass__属性不能被继承，而Bar.__class__对象的__metaclass__则可以,如果Bar使用的__metaclass__使用type()创建Bar而不是type.__new__(),子类不会继承这个行为.
"""

#__metaclass__的作用是当类创建时自动改变类.通常用于API。

#1.通过函数方法改变类:重写type函数

def upper_attr(new_class_name,new_class_parents,new_class_attr):
    uppercase_attr={}
    for name,val in new_class_attr.items():
        if not name.startswith("__"):
            uppercase_attr[name.upper()]=val
        else:
            uppercase_attr[name]=val
    return type(new_class_name,new_class_parents,uppercase_attr) #调用type函数，重写规则
__metaclass__ = upper_attr#这里影响当前模块所有的类

class Foo():
    bar = "bip"
print hasattr(Foo,"BAR")#属性全部要大写

#2.通过类的魔法方法来实现重写构建类的规则:

class UpperattrMetaclass(type):#继承type对象，重写type构建
    """#这里的new_metaclass相当于self,__new__接收一个参数作为它要改变的类对象"""
    def __new__(new_metaclass,new_class,new_class_parents,new_class_attr):        
        uppercase_attr={}
        for name,attr in new_class_attr.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()]= attr
            else:
                uppercase_attr[name]=attr
        return type.__new__(new_metaclass,new_class,new_class_parents,uppercase_attr)
#在实际生产环境中使用:
class UpperattrMetaclass(type):#继承type对象，重写type构建
    """#这里的new_metaclass相当于self,__new__接收一个参数作为它要改变的类对象"""
    def __new__(cls,clsname,bases,dct):        
        uppercase_attr={}
        for name,attr in dct.items():
            if not name.startswith("__"):
                uppercase_attr[name.upper()]= attr
            else:
                uppercase_attr[name]=attr
        return type.__new__(cls,clsname,bases,uppercase_attr)
        #或者使用super简化继承metaclass的__new__方法
        #return super(UpperattrMetaclass,cls).__new__(cls,clsname,bases,uppercase_attr)

