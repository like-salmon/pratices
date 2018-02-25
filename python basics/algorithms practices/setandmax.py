#!/usr/bin/env python
#coding:utf-8

rs={}
def parseseq(seq):
    """use set or max to find the biggest number which occurs in odd times and return itself with its times accordingly"""
    sli=list(set(seq))
    for i in sli:
        a=seq.count(i)
        rs[str(i)]=a
    print rs
    b=[i for i in rs.values() if i%2 !=0]
    c=max(b)
    for i in rs:
        if rs[i]==c:
            print "the item is :%s,and its odd times is:%d"%(i,c)
    
    
if __name__=="__main__":
    a=[1,2,3,4,5,1,2,3,4,5,32,2,3,1,1,3,4]
    parseseq(a)
